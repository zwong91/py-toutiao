#! /bin/bash
source ~/.bash_profile
export PYTHONPATH=/root/config:$PYTHONPATH
export FLASK_ENV=production
export TOUTIAO_WEB_SETTINGS=/root/config/web_deploy.py
export TOUTIAO_CELERY_SETTINGS=celery_deploy.CeleryConfig
cd /root/toutiao-backend/
workon toutiao
exec gunicorn -b 0.0.0.0:8002 --access-logfile /root/logs/access_mp.log --error-logfile /root/logs/error_mp.log mp.main:app