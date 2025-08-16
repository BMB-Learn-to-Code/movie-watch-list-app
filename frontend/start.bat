@echo off
REM Movie Watch List Frontend Starter Script (Windows)
REM This script starts the frontend server and opens it in your browser

echo 🎬 Starting Movie Watch List Frontend...
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is required but not installed.
    echo Please install Python and try again.
    pause
    exit /b 1
)

REM Get the directory where this script is located
cd /d "%~dp0"

echo 📂 Working directory: %CD%
echo 🚀 Starting frontend server on http://localhost:3000
echo.
echo ⚠️  IMPORTANT: Make sure your Flask API is running!
echo    Start it in another command prompt with: python server.py
echo    (from the main project directory)
echo.
echo 🛑 Press Ctrl+C to stop the server
echo.

REM Start the Python server
python serve.py

pause
