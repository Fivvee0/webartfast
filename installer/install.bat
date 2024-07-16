@echo off

cd app

set /p name=Name of web app: 
set /p dir=Directory that you wanna install web app: 

pip install --no-cache-dir -r requirements.txt
python webartfast.py create --name %name% --dir %dir%

echo Done!