@echo off

set "exe_path=D:\project\QT\Final-assignments\venv\Scripts\pyside6-uic.exe"

set "arg1=%1"
set "arg2=%2"

%exe_path% %arg1% -o %arg2%