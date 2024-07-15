#!/bin/bash

cd ..
cd ..

read -p "Name of web app: " name

docker build -t "$name" .

echo Done!