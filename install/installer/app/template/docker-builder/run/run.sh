#!/bin/bash

cd ..
cd ..

read -p "Name of web app: " name

docker run -p 80:80 "$name" .

echo Done!