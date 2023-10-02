#!/bin/bash

source /home/wang/.bashrc

export PYTHONPATH=/home/wang/config:$PYTHONPATH
export FLASK_ENV=production
cd /home/wang/backend-service/schedule/
workon toutiao
exec python main.py