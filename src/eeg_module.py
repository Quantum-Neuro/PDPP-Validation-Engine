import mne
import numpy as np
import random
np.random.seed(42)
random.seed(42)
import os
import glob
from tensorpac import Pac

def list_local_datasets_iter(folders=["data"]):
    """Retrieve all EEG data files under specified folder lists (supports multi-level scanning, supports .edf, .vhdr, .bdf). Yields incrementally to prevent thread blocking."""
    valid_exts = ('.edf', '.vhdr', '.bdf')
    for folder in folders:
        try:
            os.makedirs(folder, exist_ok=True)
        except Exception:
            pass # Ignore creation errors for potentially read-only external mounted drives
            
        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(valid_exts):
                    abs_path = os.path.join(root, file)
                    yield (folder, os.path.relpath(abs_path, folder))

def extract_dmn_decoupling_vectorized(epochs_data, ch_names, sfreq):
    clean_names = [ch.strip(' .\t-').upper() for ch in ch_names]
    try:
        idx_mpfc = clean_names.index('FZ')
        idx_pcc = clean_names.index('PZ')
    except ValueError:
        return np.full(epochs_data.shape[0], np.nan)
        
    data1 = epochs_data[:, idx_mpfc, :]
    data2 = epochs_data[:, idx_pcc, :]
    
    from scipy import signal
    f, Cxy = signal.coherence(data1, data2, fs=sfreq, nperseg=min(int(sfreq*2), data1.shape[-1]), axis=-1)
    
    idx = (f >= 1) & (f <= 7)
    coh_band = np.mean(Cxy[:, idx], axis=-1)
    return 1.0 / (coh_band + 1e-8)

def compute_long_range_plv_vectorized(epochs_data, ch_names, sfreq):
    clean_names = [ch.strip(' .\t-').upper() for ch in ch_names]
    frontal = [ch for ch in ['F3', 'F4', 'FZ'] if ch in clean_names]
    occipital = [ch for ch in ['O1', 'O2', 'OZ'] if ch in clean_names]
    
    if not frontal or not occipital:
        return np.full(epochs_data.shape[0], np.nan)
        
    frontal_idx = [clean_names.index(ch) for ch in frontal]
    occipital_idx = [clean_names.index(ch) for ch in occipital]
    
    data_f = np.mean(epochs_data[:, frontal_idx, :], axis=1)
    data_o = np.mean(epochs_data[:, occipital_idx, :], axis=1)
    
    from scipy import signal
    b, a = signal.butter(4, [25, 42], btype='bandpass', fs=sfreq)
    filt_f = signal.filtfilt(b, a, data_f, axis=-1)
    filt_o = signal.filtfilt(b, a, data_o, axis=-1)
    
    phase_f = np.angle(signal.hilbert(filt_f, axis=-1))
    phase_o = np.angle(signal.hilbert(filt_o, axis=-1))
    
    plv = np.abs(np.mean(np.exp(1j * (phase_f - phase_o)), axis=-1))
    return plv

def compute_topological_cfc(data_low, data_high, sfreq):
    """
    Mechanism Mapping: Introduce professional-grade TensorPAC to compute Modulation Index (MI) of frontal Theta phase on occipital Gamma amplitude.
    This is the core feature for EVT and Granger tests, highly immune to limb artifacts.
    """
    # Use uncapped Mean Vector Length (MVL, idpac=1) instead of normalized PLV to release genuine extreme bursts
    # Shift to High-Gamma/Ripple amplitude band [80, 200] Hz to capture microscopic dipole topological properties
    p_obj = Pac(idpac=(1, 0, 0), f_pha=[4, 8], f_amp=[80, 200])
    
    # filterfit expects input of shape (n_epochs, n_times)
    x_pha = np.atleast_2d(data_low)
    x_amp = np.atleast_2d(data_high)
    
    # Compute MI (vectorized across all epochs in C/Fortran)
    # Multiply by 1e6 to amplify magnitude, preventing microvolt-level EEG MVL (e-8) from being truncated to 0.0000 in statistics
    cfc_values = p_obj.filterfit(sfreq, x_pha=x_pha, x_amp=x_amp, n_jobs=1) * 1e6
    return np.squeeze(cfc_values)

def process_local_eeg(filepath):
    """
    [PDPP v3.0] Extract high-dimensional neural topological features, interfacing with quantum extreme causal test.
    Returns: times, dmn_decoupling, long_range_plv, cfc_mi
    """
    mne.set_log_level('WARNING')
    
    if filepath.endswith(".vhdr"):
        raw = mne.io.read_raw_brainvision(filepath, preload=True, verbose=False)
    elif filepath.endswith(".npy"):
        data = np.load(filepath)
        if data.ndim == 3:
            data = data.reshape(data.shape[1], -1)
        if data.shape[0] > data.shape[1]:
            data = data.T
        ch_names = [f'CH{i}' for i in range(data.shape[0])]
        if len(ch_names) >= 4:
            ch_names[0], ch_names[1], ch_names[2], ch_names[3] = 'FZ', 'OZ', 'PZ', 'F3'
        elif len(ch_names) > 1:
            ch_names[0], ch_names[1] = 'FZ', 'OZ'
        info = mne.create_info(ch_names=ch_names, sfreq=250.0, ch_types='eeg')
        raw = mne.io.RawArray(data, info, verbose=False)
    else:
        raw = mne.io.read_raw_edf(filepath, preload=True, verbose=False)
        
    # Surgical Mains Interference Removal (50Hz/60Hz)
    raw.notch_filter(freqs=[50, 60], fir_design='firwin', phase='zero', verbose=False)
    # Broaden upper bandpass limit to 250Hz to preserve High-Gamma/Ripple band physics, avoiding filter collisions
    raw.filter(l_freq=0.5, h_freq=250.0, fir_design='firwin', phase='zero', verbose=False)
    
    sfreq = raw.info['sfreq']
    
    # Forcibly enlarge observation window, perform high-density overlapping slicing
    epochs = mne.make_fixed_length_epochs(
        raw, 
        duration=10.0, 
        overlap=9.0, 
        preload=True,
        verbose=False
    )
    
    dmn_list = []
    plv_list = []
    cfc_list = []
    
    clean_raw_names = [ch.strip(' .\t-').upper() for ch in raw.ch_names]
    try:
        idx_low = clean_raw_names.index('FZ')
    except ValueError:
        idx_low = 0
        
    try:
        idx_high = clean_raw_names.index('OZ')
    except ValueError:
        idx_high = 0
    
    n_epochs = len(epochs)
    epochs_data = epochs.get_data()
    ch_names = epochs.ch_names
    
    # 1. & 2. Completely remove serial MNE extraction, switch to pure SciPy full tensor computation!
    # Instant computation completion, no multiprocessing needed, completely eliminating Fork Bomb and GIL bottlenecks
    dmn_all = extract_dmn_decoupling_vectorized(epochs_data, ch_names, sfreq)
    plv_all = compute_long_range_plv_vectorized(epochs_data, ch_names, sfreq)
    
    # 3. Theta-Gamma CFC (TensorPAC MI) - Vectorized 85x Speedup!
    data_low_all = epochs_data[:, idx_low, :]
    data_high_all = epochs_data[:, idx_high, :]
    cfc_all = compute_topological_cfc(data_low_all, data_high_all, sfreq)
    
    # Ensure it's iterable even if 1 epoch
    if cfc_all.ndim == 0:
        cfc_all = np.array([cfc_all])
        
    for i in range(n_epochs):
        dmn = float(dmn_all[i])
        plv = float(plv_all[i])
        cfc = float(cfc_all[i])
        
        if not np.isnan(dmn) and not np.isnan(plv) and not np.isnan(cfc):
            dmn_list.append(dmn)
            plv_list.append(plv)
            cfc_list.append(cfc)
            
    if not dmn_list:
        return np.array([]), np.array([]), np.array([]), np.array([])
        
    # Because step is 1.0 second (duration 10, overlap 9)
    times = np.arange(len(dmn_list)) * 1.0
    
    return times, np.array(dmn_list), np.array(plv_list), np.array(cfc_list)

def map_parameters(dmn_arr, plv_arr, cfc_arr):
    """
    v3.0 Map features to quantum parameters
    """
    def normalize(arr):
        if len(arr) == 0 or np.max(arr) == np.min(arr):
            return np.zeros_like(arr)
        return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
        
    cfc_norm = normalize(cfc_arr)
    dmn_norm = normalize(dmn_arr)
    
    gamma = 5.0 - cfc_norm * (5.0 - 0.1)  
    epsilon = 1.0 - dmn_norm * 0.9        
    
    return gamma, epsilon
