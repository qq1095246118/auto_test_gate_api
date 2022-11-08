#!/bin/bash
package_url=$(cat utility/application.py | grep package_path | grep -v "#" | awk -F "=" '{print $2}' |sed  $'s/\'//g' )
wget -q $package_url
package_file=$(echo $package_url | awk -F "/" '{print $NF}')
echo $package_file
tar -xf $package_file
images=`docker images | grep -v '10.1.5.103\|redis' | awk '{print $3}' | grep -v IMAGE`
cp -r  install/dist/* install/scripts/dist
cd install/scripts
docker-compose -f bct-compose.yml down
docker rmi $images
cd airflowfile/
cp -r ../airflow ./
echo "start building airflow docker image from $(pwd)"
docker build -t bct-airflow:1.10.3 ./
cd ../nginx
cp -r ../dist ./
echo "start building nginx docker image from $(pwd)"
docker build -t bct-nginx:1 ./
cd ../bct-server
cp -r ../../bin ./
cp ../../bct.config.js ./
echo "start building bct docker image from $(pwd)"
docker build -t bct-server:latest ./
cd ../postgres/
echo "start building postgresql docker image from $(pwd)"
docker build -t bct-postgres:9.6 ./
cd ../
echo "stop all containers"
docker-compose -f bct-compose.yml down
echo "start all containers"
docker-compose -f bct-compose.yml up -d

ret=1
while [[ $ret -ne 0 ]]
do
    echo "wait 10 seconds for services to start up"
	sleep 10
	TOKEN_ADMIN=`curl -s -H "content-type: application/json" -X POST -d '{"userName": "YWRtaW4=", "password": "MTIzNDU="}' http://localhost:80/auth-service/users/login | jq -r '.token'`
	if [[ -z "$TOKEN_ADMIN" ]] || [[ ${TOKEN_ADMIN} = "null" ]]; then
		ret=1
	else
		ret=0
	fi
done
echo "bct-server is up"
pwd
cd initialize/minimum
./init_min_system.sh
