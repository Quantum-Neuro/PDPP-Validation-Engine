import sys
import os
import subprocess

def ensure_dependencies():
    try:
        import pkg_resources
        req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
        if os.path.exists(req_file):
            with open(req_file, 'r') as f:
                requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            pkg_resources.require(requirements)
    except Exception as e:
        print(f"Missing dependencies or version mismatch detected ({e}). Starting automatic fix...")
        install_script = os.path.join(os.path.dirname(__file__), "src", "install_deps.py")
        subprocess.check_call([sys.executable, install_script])
        print("Fix applied. Restarting main engine...")
        os.execv(sys.executable, [sys.executable] + sys.argv)

ensure_dependencies()

import glob
import numpy as np
import random
np.random.seed(42)
random.seed(42)
from src.validation_engine import run_validation_and_generate_report

def main():
    print("========================================")
    print(" PDPP Extreme Causal Validation Engine")
    print("========================================")
    
    data_dir = os.path.join(os.getcwd(), "data")
    if not os.path.exists(data_dir):
        print(f"[Warning] Directory {data_dir} not found.")
        
    active_dataset_name = "Real Dataset"
    eeg_files = glob.glob(f"{data_dir}/**/*.vhdr", recursive=True) + glob.glob(f"{data_dir}/**/*.npy", recursive=True) + glob.glob(f"{data_dir}/**/*.edf", recursive=True)
    eeg_files.sort()
    
    if not eeg_files:
        print("[Info] No EEG data files found. Triggering automatic sample data download...")
        try:
            from src import download_sample_data
            download_sample_data.fetch_sample_data(data_dir)
            eeg_files = glob.glob(f"{data_dir}/**/*.vhdr", recursive=True) + glob.glob(f"{data_dir}/**/*.npy", recursive=True) + glob.glob(f"{data_dir}/**/*.edf", recursive=True)
            eeg_files.sort()
        except Exception as e:
            print(f"[Warning] Auto-download failed or script missing: {e}")
            
    # Fallback to Sample Dataset if download failed (e.g. no internet)
    if not eeg_files:
        toy_dir = os.path.join(os.getcwd(), "data_sample")
        if os.path.exists(toy_dir):
            print("[Warning] Network download failed. Falling back to the offline Sample Dataset (data_sample)...")
            eeg_files = glob.glob(f"{toy_dir}/**/*.npy", recursive=True)
            eeg_files.sort()
            active_dataset_name = "Sample Dataset (Fallback)"
            
    if not eeg_files:
        print("[Error] No EEG data files found, and Sample Dataset is missing. Please add data manually.")
        return
    else:
        print(f"Found {len(eeg_files)} data files in [{active_dataset_name}]. Preparing for analysis...")

    import select
    
    print("\n" + "="*40)
    print(" Frequency Band Selection")
    print("="*40)
    print("1: [30-70 Hz] Gamma Band")
    print("   (Standard Methodological Benchmark - Expects Negative Interception)")
    print("2: [80-200 Hz] High-Gamma / Ripple Band")
    print("   (Deep Microscopic Topology - Probing Genuine Quantum Coherence)")
    print("Select the analysis frequency band (1 or 2) [Auto-defaulting to 1 in 5 seconds]: ", end='', flush=True)
    
    i, o, e = select.select([sys.stdin], [], [], 5)
    if i:
        choice = sys.stdin.readline().strip()
    else:
        print("\nTimeout reached. Defaulting to 1.")
        choice = '1'
        
    if choice not in ['1', '2']:
        choice = '1'
    
    if choice == '1':
        os.environ['PDPP_FREQ_MODE'] = 'gamma'
        os.environ['PDPP_ENABLE_ELORETA'] = '0'
        print("-> [Info] Selected Gamma Band (30-70 Hz). Fast ICA enabled. Source Localization bypassed.")
    else:
        os.environ['PDPP_FREQ_MODE'] = 'high_gamma'
        print("-> [Info] Selected High-Gamma Band (80-200 Hz) with 250 Hz Bandpass.")
        
        # Optional Source Localization for High-Gamma
        print("Enable 3D Source Localization (eLORETA)? Requires ~200MB MRI template download. (y/N) [Auto-defaulting to N in 5 seconds]: ", end='', flush=True)
        i2, o2, e2 = select.select([sys.stdin], [], [], 5)
        if i2:
            loreta_choice = sys.stdin.readline().strip().lower()
        else:
            print("\nTimeout reached. Defaulting to N.")
            loreta_choice = 'n'
            
        if loreta_choice == 'y':
            os.environ['PDPP_ENABLE_ELORETA'] = '1'
            print("-> [Info] eLORETA Source Localization enabled.")
        else:
            os.environ['PDPP_ENABLE_ELORETA'] = '0'
            print("-> [Info] Source Localization bypassed.")
            
    print("="*40 + "\n")

    report_dir = os.path.join(os.getcwd(), "Report")
    
    try:
        report_path = run_validation_and_generate_report(eeg_files, report_dir)
        print(f"\n[Success] Validation execution completed!")
        print(f"Generated evaluation report saved at: {report_path}")
    except Exception as e:
        print(f"\n[Error] An exception occurred during execution: {e}")

if __name__ == "__main__":
    main()
