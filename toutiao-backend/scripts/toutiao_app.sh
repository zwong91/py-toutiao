#! /bin/bash
source ~/.bashrc
export FLASK_ENV=production
cd /home/wz/hm-toutiao/toutiao-backend/
workon toutiao
exec gunicorn -b 0.0.0.0:8000 --access-logfile /home/wz/logs/access_app.log --error-logfile /home/wz/logs/error_app.log toutiao.main:app