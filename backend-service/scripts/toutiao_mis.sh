#!/bin/bash

source /home/wang/.bashrc

export PYTHONPATH=/home/wang/config:$PYTHONPATH
export FLASK_ENV=production
export TOUTIAO_WEB_SETTINGS=/home/wang/config/web_deploy.py
export TOUTIAO_CELERY_SETTINGS=celery_deploy.CeleryConfig
cd /home/wang/py-toutiao/backend-service/
workon toutiao
exec gunicorn -b 0.0.0.0:8003\
    --access-logfile /home/wang/py-toutiao/logs/access_mis.log\
    --error-logfile /home/wang/py-toutiao/logs/error_mis.log\
    mis.main:app