#docker network inspect redis-cluster
ip=127.0.0.1
redis-cli  -a 1234 --cluster create ${ip}:7001 ${ip}:7002 ${ip}:7003 ${ip}:7004 ${ip}:7005 ${ip}:7006  --cluster-replicas 1
