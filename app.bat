@echo off
pushd %~dp0

pip install .\requirements.py

python .\app.py
pause
