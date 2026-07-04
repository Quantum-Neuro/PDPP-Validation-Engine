#!/bin/bash
cd "$(dirname "$0")"

echo "========================================"
echo " Starting PDPP Causal Inference Engine..."
echo "========================================"

if [ ! -d ".venv" ]; then
    echo "[Security Isolation] First run detected. Creating an isolated virtual environment (.venv)..."
    echo "This ensures your global Python environment remains unaffected!"
    python3 -m venv .venv
fi

source .venv/bin/activate

python main.py

echo ""
echo "Execution finished. Press any key to close this window..."
read -n 1 -s
osascript -e 'tell application "Terminal" to close front window' > /dev/null 2>&1 &
exit
