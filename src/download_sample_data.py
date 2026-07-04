import os
import urllib.request
import ssl
import sys

def download_file_with_progress(url, dest_path, ctx):
    tmp_path = dest_path + ".tmp"
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            # 15-second timeout to prevent hanging on network drop
            with urllib.request.urlopen(url, context=ctx, timeout=15) as response:
                total_size = int(response.getheader('Content-Length', 0))
                downloaded = 0
                chunk_size = 8192
                
                with open(tmp_path, 'wb') as out_file:
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        out_file.write(chunk)
                        downloaded += len(chunk)
                        
                        if total_size > 0:
                            percent = int(downloaded * 100 / total_size)
                            bar_length = 30
                            filled = int(bar_length * downloaded / total_size)
                            bar = '█' * filled + '-' * (bar_length - filled)
                            sys.stdout.write(f"\r    [{bar}] {percent}% ({downloaded/(1024*1024):.2f}/{total_size/(1024*1024):.2f} MB)")
                            sys.stdout.flush()
                        else:
                            sys.stdout.write(f"\r    Downloaded {downloaded/(1024*1024):.2f} MB")
                            sys.stdout.flush()
                            
                sys.stdout.write("\n")
                
            # Rename tmp to final only upon complete success (Atomic operation)
            os.rename(tmp_path, dest_path)
            return True
            
        except Exception as e:
            if os.path.exists(tmp_path):
                os.remove(tmp_path) # Clean up corrupted partial files
            
            if attempt < max_retries - 1:
                print(f"\n    [Retry {attempt+1}/{max_retries}] Network error ({e}). Retrying in 2 seconds...")
                import time
                time.sleep(2)
            else:
                raise e

def fetch_sample_data(data_dir):
    print("\n========================================")
    print(" Downloading Sample Data (OpenNeuro ds003816)")
    print("========================================")
    
    base_url = "https://s3.amazonaws.com/openneuro.org/ds003816"
    
    # 24 files total: 4 sessions x 6 files (BIDS format)
    sessions = [
        ("sub-11lt", "ses-05"),
        ("sub-11lt", "ses-06"),
        ("sub-23st", "ses-01"),
        ("sub-24st", "ses-01")
    ]
    
    task = "task-LKMOther"
    extensions = [
        "eeg.vhdr", "eeg.vmrk", "eeg.eeg", 
        "eeg.json", "events.tsv", "channels.tsv"
    ]
    
    # Disable SSL verification to prevent potential certificate issues across different OS
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    success_count = 0
    total_expected = len(sessions) * len(extensions)

    for sub, ses in sessions:
        target_dir = os.path.join(data_dir, sub, ses, "eeg")
        os.makedirs(target_dir, exist_ok=True)
        
        for ext in extensions:
            filename = f"{sub}_{ses}_{task}_{ext}"
            url = f"{base_url}/{sub}/{ses}/eeg/{filename}"
            save_path = os.path.join(target_dir, filename)
            
            if not os.path.exists(save_path):
                print(f"-> Downloading: {filename}")
                try:
                    download_file_with_progress(url, save_path, ctx)
                    success_count += 1
                except Exception as e:
                    print(f"\n[Error] Failed to download {filename} (Timeout or Network Drop): {e}")
                    raise Exception("Network failure during auto-download.")
            else:
                success_count += 1
                
    print(f"========================================")
    print(f" Download Complete: {success_count}/{total_expected} files ready.")
    print(f"========================================\n")
