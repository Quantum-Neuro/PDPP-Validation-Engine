import sys
import subprocess
import os

def install_requirements():
    req_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'requirements.txt')
    print(f"Reading and installing dependencies: {req_file}")
    if not os.path.exists(req_file):
        print("requirements.txt not found!")
        return
        
    print("Attempting to install via official PyPI (Global)...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", req_file
        ])
        print("Installation via official PyPI succeeded.")
        return
    except subprocess.CalledProcessError:
        print("Official PyPI failed (possible network issue). Switching to Tsinghua TUNA mirror (for Mainland China users)...")
        
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", req_file,
            "-i", "https://pypi.tuna.tsinghua.edu.cn/simple",
            "--trusted-host", "pypi.tuna.tsinghua.edu.cn"
        ])
        print("Installation via Tsinghua mirror succeeded.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies even with mirror: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
