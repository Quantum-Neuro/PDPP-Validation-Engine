#!/bin/bash
cd "$(dirname "$0")"

echo "========================================"
echo " Starting PDPP Causal Inference Engine..."
echo "========================================"

if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
else
    echo "[Error] Python environment not found. Please install Python 3.9+."
    read -p "Press Enter to exit..."
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "[Security Isolation] First run detected. Creating an isolated virtual environment (.venv)..."
    echo "This ensures your global Python environment remains unaffected!"
    $PYTHON_CMD -m venv .venv
fi

source .venv/bin/activate

python main.py

echo ""
echo "Execution finished. Press Enter to close this window..."
read
