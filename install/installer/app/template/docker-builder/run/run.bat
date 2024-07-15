@echo off

cd ..
cd ..

set /p name=Name of Docker Image: 

docker run -p 80:80 %name% .

echo Done!