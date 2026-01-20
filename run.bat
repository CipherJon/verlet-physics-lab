@echo off
:: Quick launch script for the project (Windows)
set PYTHONPATH=%PYTHONPATH%;%~dp0src
python main.py
pause
