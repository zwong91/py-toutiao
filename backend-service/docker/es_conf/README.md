### docker-compose 方式

```sh
docker-compose up -d
docker-compose stop
docker-compose restart

docker ps
docker stop $(docker ps -a -q)

docker inspect -f='{{.Name}} {{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}} {{.HostConfig.PortBindings}}' $(docker ps -aq)
```

- Web 访问

```sh
docker-compose up -d && docker-compose logs -f
docker-compose ps

http://localhost:9200/ 这是es的基本信息
http://localhost:5601/ 这是kibana 控制台
```
