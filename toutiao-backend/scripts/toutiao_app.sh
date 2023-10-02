#! /bin/bash
source ~/.bash_profile
export FLASK_ENV=production
cd $HOME/py-toutiao/toutiao-backend/
workon toutiao
exec gunicorn -b 0.0.0.0:8000 --access-logfile $HOME/py-toutiao/toutiao-backend/toutiao/logs/access_app.log --error-logfile $HOME/py-toutiao/toutiao-backend/toutiao/logs/error_app.log toutiao.main:app