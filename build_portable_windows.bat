@echo off
setlocal
cd /d "%~dp0"
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py -m PyInstaller --noconfirm --clean --onefile --windowed --name NyomsVegetasiPantai app.py
echo Selesai. Berkas portable ada di dist\NyomsVegetasiPantai.exe
pause
