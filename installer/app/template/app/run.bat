@echo off

cd ../python

pip install --no-cache-dir -r requirements.txt
python app.py

echo Done!