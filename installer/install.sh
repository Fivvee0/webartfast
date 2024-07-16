#!/bin/bash

cd app

read -p "Name of web app: " name
read -p "Directory that you want to install web app: " dir

pip install --no-cache-dir -r requirements.txt
python webartfast.py --name "$name" --dir "$dir"

echo "Done!"