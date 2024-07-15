@echo off

cd ..
cd ..

set /p name=Name of Docker Image: 

docker build -t %name% .

echo Done!