@echo off
REM Project Eclipse Setup Script for Windows

echo =======================================
echo PROJECT ECLIPSE: Horror Survival Setup
echo =======================================
echo.

REM Check Python
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Python version: %PYTHON_VERSION%
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat
echo.

REM Create asset directories
echo Creating asset directories...
if not exist "assets\textures" mkdir assets\textures
if not exist "assets\models" mkdir assets\models
if not exist "assets\sounds" mkdir assets\sounds
if not exist "assets\ui" mkdir assets\ui
echo Asset directories created
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo.

echo =======================================
echo Setup complete!
echo Run: python main.py
echo =======================================
pause
