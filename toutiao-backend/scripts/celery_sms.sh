#!/bin/bash

source /home/wang/.bashrc

export PYTHONPATH=/home/wang/config:$PYTHONPATH
export FLASK_ENV=production
export TOUTIAO_WEB_SETTINGS=/root/config/web_deploy.py
export TOUTIAO_CELERY_SETTINGS=celery_deploy.CeleryConfig
cd /home/wang/py-toutiao/toutiao-backend/common
workon toutiao
exec celery -A celery_tasks.main worker -l info -Q sms