### 测试节点软件包service更新、日志上报的文件系统服务，用于测试节点软件包更新，日志上传, 测试用例路由转发服务
使用python3 + Flask + redis实现。

部署步骤：

+ 安装python依赖包
```
cd node_tester_server
pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/ 
```
+ 启动服务 gunicorn
```
cd /opt/node_tester/server  多开分流
// 直接启动
gunicorn -b 127.0.0.1:12000 api:app  >> server.log &
// 后台启动
nohup gunicorn -b 127.0.0.1:12000 api:app  >> server.log 2>&1&
```
+ 常用操作
```
http://bdttest.tinyappcloud.com/index.html#/
scp root@ip:/sourcepath root@ip:/destpath
netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'
ls -lR|grep "^-"| wc -l

cat report_log/2018-07-02.log | grep queryCmd | grep "}}, \"peerid\": \"15232783589-TZpJdFer" | grep "Jul 2 00"
垃圾日志信息
"13794462011_xxx" "1.1" "{\"seedPeers\": [{\"peerid\":\"SEED_DHT_PEER_10000\", \"eplist\":[\"4@192.168.200.175@10000@u\", \"4@192.168.200.175@10010@t\"]},{\"peerid\": \"SEED_DHT_PEER_10000_IPV6\", \"eplist\": [\"6@240e:fa:1143:bd00::16e@10000@u\", \"6@240e:fa:1143:bd00::16e@10010@t\"]}]}"
垃圾账号信息
http://www.gct.one/Ch/bdt-2/
blockchain NPM
username:buckychain
password:EAR6bXKlLP
email:blockchain@buckyos.com
```