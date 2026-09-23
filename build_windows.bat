@echo off
setlocal

py -m pip install -r requirements.txt
py -m PyInstaller --onefile --windowed --name ClassroomDemo ^
  --add-data "assets;assets" classroom_demo.py

echo.
echo Built dist\ClassroomDemo.exe
pause