#!/bin/sh

clear
docker-compose up -d --build

sleep 5

echo "---------------------"
echo Direct
curl http://localhost:8000/

echo "---------------------"
echo Over 1
curl http://localhost:8083/

echo "---------------------"
echo Over 2
curl http://localhost:8082/

echo "---------------------"
echo Over 3
curl http://localhost:8081/

echo "---------------------"
echo Add header
curl -H "X-Forwarded-For: 1.1.1.1" http://localhost:8081/

docker-compose down


