import mne
import numpy as np
import os

def perform_source_localization(raw, method='eLORETA'):
    """
    Perform spatial topological localization on the EEG data.
    Maps scalp High-Gamma / Ripple signals back to the cortical source space (e.g., DMN nodes).
    """
    print(f"\n[Source Localization] Initializing {method} mapping to 3D cortical space...")
    
    try:
        # Step 1: Set up the source space using the generic 'fsaverage' template
        # Note: This requires the fsaverage dataset to be downloaded (~200MB)
        subjects_dir = mne.datasets.sample.data_path() / 'subjects'
        subject = 'fsaverage'
        
        print("[Source Localization] Loading standard 'fsaverage' anatomy...")
        fs_dir = mne.datasets.fetch_fsaverage(verbose=False)
        subjects_dir = os.path.dirname(fs_dir)
        
        # In a real pipeline, we need to map the EEG electrodes to standard 10-20 positions.
        montage = mne.channels.make_standard_montage('standard_1020')
        raw.set_montage(montage, on_missing='ignore')
        
        src_file = os.path.join(fs_dir, 'bem', 'fsaverage-ico-5-src.fif')
        bem_file = os.path.join(fs_dir, 'bem', 'fsaverage-5120-5120-5120-bem-sol.fif')
        
        if not os.path.exists(src_file) or not os.path.exists(bem_file):
            print("[Warning] fsaverage BEM/SRC files missing locally. Cannot compute forward solution.")
            return None
            
        print("[Source Localization] Computing Forward Solution (Leadfield Matrix)...")
        fwd = mne.make_forward_solution(raw.info, trans='fsaverage', src=src_file, bem=bem_file, eeg=True, meg=False, verbose=False)
        
        print("[Source Localization] Computing Data Covariance and eLORETA Inverse Operator...")
        # We compute empirical covariance directly from the continuous raw data
        noise_cov = mne.compute_raw_covariance(raw, tmin=0, tmax=None, verbose=False)
        inverse_operator = mne.minimum_norm.make_inverse_operator(raw.info, fwd, noise_cov, loose=0.2, depth=0.8, verbose=False)
        
        # Apply eLORETA algorithm to project 80-200 Hz sensor data back to 3D cortical space
        stc = mne.minimum_norm.apply_inverse_raw(raw, inverse_operator, lambda2=1.0/9.0, method=method, verbose=False)
        
        print(f"[Source Localization] {method} successfully projected to {stc.data.shape[0]} cortical nodes (e.g., DMN network).")
        return stc
        
    except Exception as e:
        print(f"[Error] Source localization failed: {e}")
        return None
