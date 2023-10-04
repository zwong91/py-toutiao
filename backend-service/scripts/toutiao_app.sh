#!/bin/bash
# load virtualenvwrapper for python (after custom PATHs)
source /home/wang/.local/bin/virtualenvwrapper.sh

export FLASK_ENV=production
cd  /home/wang/py-toutiao/backend-service/
workon toutiao
exec gunicorn -b 0.0.0.0:8000\
    --access-logfile /home/wang/py-toutiao/backend-service/logs/access_app.log\
    --error-logfile /home/wang/py-toutiao/backend-service/logs/error_app.log\
    toutiao.main:app