## 部署 gm_tool:

基于 Django 4.2.5 + sqlite3 + tcp socket + mysql

````sh
python虚拟环境安装
pip3 install virtualenv virtualenvwrapper
sudo apt install --reinstall virtualenv
# ~/.bashrc 添加如下:
```sh
# virtualenvwrapper存放虚拟环境目录
export WORKON_HOME="~/.virtualenvs"
export PROJECT_HOME=$HOME/py-toutiao
export VIRTUALENVWRAPPER_PYTHON="/usr/bin/python3"
# bin/virtualenvwrapper.sh
source ~/.local/bin/virtualenvwrapper.sh


lsvirtualenv
mkvirtualenv gmt -p python3
rmvirtualenv gmt
workon gmt
deactivate

````

- Django 设置账号密码

```sh
python3 manage.py createsuperuser
python manage.py migrate
python manage.py migrate --run-syncdb

admin/123456
http://127.0.0.1:9300/admin
```

- 复制 python_test/python_conf.py.dist 为 python_conf.py，修改文件中的配置数据，然后移动至 dgame_svr/python_test/inc 目录下 新区配置文件
- 在 gm_tool 目录下执行 nohup python3 manage.py runserver 0.0.0.0:9300 &
