@echo off
setlocal
cd /d "%~dp0"
py app.py
if errorlevel 1 pause
