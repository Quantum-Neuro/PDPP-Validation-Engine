@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo  Starting PDPP Causal Inference Engine...
echo ========================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [Error] Python is not installed on your system or not in PATH.
    echo Please download and install Python 3.9+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b
)

if not exist ".venv\" (
    echo [Security Isolation] First run detected. Creating an isolated virtual environment (.venv)...
    echo This ensures your global Python environment remains unaffected!
    python -m venv .venv
)

call .venv\Scripts\activate.bat

python main.py

echo.
echo Execution finished. Press any key to close this window...
pause >nul
