# 基于Ubuntu20.04 python 环境
* sudo apt-get update
* sudo apt-get upgrade  #Optional
* sudo apt install python3-pip

* sudo apt-get install xvfb

* pip install requests tqdm  bs4  selenium  pyvirtualdisplay  lxml  pyinstaller

* pip3 install --upgrade requests
* pip install fake_useragent


***要求运行环境能访问www.google.com, 要求必须先启动代理池***

# selenium 使用chromium driver 依赖chromium-browser
* sudo apt-get install chromium-browser
* chromium-browser --version

http://chromedriver.storage.googleapis.com/index.html


https://2captcha.com/  付费打码平台

# 设置钱包地址
export WALLET_ADDRESS=t3upqg4vr5o6rbku237puwf5iouryqzvk63s5v7njovpln5njahlxujsnvag26zoweozvpgdhk74zopsk5ykoq
python3 faucet.get_fil_proxy.py

//*[@id="funds-form"]/input

//*[@id="g-recaptcha-response"]

{"status":1,"request":"70060415522"}

# 打包程序
* pyinstaller -F faucet.get_fil_proxy.py 输出到dist

# 程序运行环境
* snap 安装 chromium-browser
* 设置环境变量 `export WALLET_ADDRESS=t3upqg4vr5o6rbku237puwf5iouryqzvk63s5v7njovpln5njahlxujsnvag26zoweozvpgdhk74zopsk5ykoq`
* 执行dist 目录下二进制文件
* 有python 编译环境, 直接执行`faucet_get_fil_proxy.sh`, 里面有一些钱包地址可编辑

# 目前爬fil测试币成功率不高, 会被anti-spam掉, 用自建爬虫动态IP代理池提高成功率
# 海外爬虫代理IP池，付费代理池, 自建代理池
* http://www.luminati-cn.net/hi
* https://luminati-china.biz/?gspk=amluZ2hhbzI1NDQ&gsxid=TON501k6a2C3&utm_source=affiliates&utm_campaign=amluZ2hhbzI1NDQ&lang=zh-hans
  
* https://github.com/jhao104/proxy_pool.git
