#!/bin/bash

source /home/wang/.bashrc

export PYTHONPATH=/home/wang/config:$PYTHONPATH
export FLASK_ENV=production
export TOUTIAO_WEB_SETTINGS=/home/wang/config/web_deploy.py
export TOUTIAO_CELERY_SETTINGS=celery_deploy.CeleryConfig
cd /home/wang/backend-service/im/
workon toutiao
exec python main.py 8001