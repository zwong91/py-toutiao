#########################################################################
# File Name: faucet_get_fil.sh
# Author: wz
# mail: wangzhi@buckyos.com
# Created Time: Fri 14 April 2022 14:09:41 PM CST
#########################################################################
#!/bin/bash

faucet_path=./faucet.get_fil_proxy.py
# Colorefull print
function green_print()
{
    local text=$@

    echo ""
    echo -e "\033[1m\033[32m[$text]\033[0m"   # 绿色加粗, 并复原
    # echo ""
}
function blue_print()
{
    local text=$@

    # echo ""
    echo -e "\033[1m\033[36m[$text]\033[0m"   # 蓝色加粗, 并复原
    # echo ""
}
function blue_print2()
{
    local text=$@

    # echo ""
    echo -e "\033[36m[$text]\033[0m"   # 蓝色, 并复原
    # echo ""
}

arr=(
"t3rpunoufdzkffxqdobespfpbelhyszdfqg7xhudxd5ec5jb3dip535d26yfon35ikokx6zvj6qalgjwdcvmvq"
"t3rtigrybllmbqu6gtmiu4wbl572xqshwu5y42f3sg4wgbkm64jd2ve7532q2v2lwcfubsfwrvvq5cj4fs6drq"
"t3wrebfr6yrtq453hxqqb4f7htrz3ndz4oijjizoh3cclsazcts7hpz6o6xbc5i4x27ncffdm6lqg4kapzxgsa"
"t1fji5meajeoa3fdl6e7jygojwguhbjuksbq6frci"
"t3tcnwqzq7ur6elf244e7zsagcmmknqbquq2ubknyzhnvwfo36mzcn35meb3mfiuk4jemj4mpa2cd3tgajd36a"
"t3uga7ahlfljbhcund4d65dgrgdndii2moxz46gkm6q6ao74iuspkhlbx5toj4ujjfmgziy2asakbgvldcztmq"
"t3uhyu73xj6t3qwjcrlmn7p5x4zmf2bu54r6m4nexjyxtyzm4a4ntuz7uloobtbu445b55k2modlkfosowrl5q"
"t3vqrhb636cjjioydbmwqxjoiwombtxj5bmsob527svamz2d4nnvaur6wohfouofqnn6irz4a5vw2hujeq7xgq"
)

green_print "faucet fil process starting..."
tm=10 # 10 min for each round
amount=100 # calibration default send 100FIL once time
while (true)
do

    t=$(date +%Y_%m_%d_%H_%M)
    blue_print "[${t}]:"
    #for 遍历数组
    for addr in ${arr[@]}
    do
        export WALLET_ADDRESS=$addr
        blue_print2 "send to [$addr] ${amount} fil!"
        blue_print "${faucet_path}"
        python3 "${faucet_path}"
    done
    
    echo -e ""
    blue_print2 "Waitting ${tm} minutes..."
    #sleep 10
    sleep ${tm}m

done
echo -e ""
