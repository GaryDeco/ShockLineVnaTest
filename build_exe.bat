@echo off

REM This builds executable to run from windows desktop icon. It only needs to be built once or when script is updated
REM This is curently a manual operation. 

REM Build yourscript.exe for yourscript.py using pyinstaller **(requires full path reference to pyinstaller.exe
REM Run this script or copy below and paste into cmd window. 
REM pyinstaller must be installed using python pip -- pip install pyinstaller

C:\Users\gary.decosmo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe --onefile --noconsole main.py