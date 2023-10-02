#!/bin/bash
# load virtualenvwrapper for python (after custom PATHs)
venvwrap="virtualenvwrapper.sh"
/usr/bin/which -a $venvwrap
if [ $? -eq 0 ]; then
    venvwrap=`/usr/bin/which $venvwrap`
    source $venvwrap
fi

export FLASK_ENV=production
cd  /home/wang/py-toutiao/backend-service/
workon toutiao
exec gunicorn -b 0.0.0.0:8000\
    --access-logfile /home/wang/py-toutiao/backend-service/logs/access_app.log\
    --error-logfile /home/wang/py-toutiao/backend-service/logs/error_app.log\
    toutiao.main:app