#!/bin/bash

source /home/wang/.bashrc

export PYTHONPATH=/home/wang/py-toutiao/config:$PYTHONPATH
export FLASK_ENV=production
export TOUTIAO_WEB_SETTINGS=/home/wang/py-toutiao/config/web_deploy.py
export TOUTIAO_CELERY_SETTINGS=celery_deploy.CeleryConfig
cd /home/wang/py-toutiao/toutiao-backend/
workon toutiao
exec gunicorn -b 0.0.0.0:8002\
    --access-logfile /home/wang/py-toutiao/logs/access_mp.log\
    --error-logfile /home/wang/py-toutiao/logs/error_mp.log\
    mp.main:app