#!/bin/bash
#*pip3 install pipenv
#*pipenv install
pipenv shell
#*pipenv install flask
#*pipenv install pytest
#*export FLASK_APP=hello
export FLASK_ENV=development
export FLASK_APP=urlshort
flask run
#*pytest
#*flask run --host=0.0.0.0
#*pipenv install gunicorn
#*gunicorn "urlshort:create_app()" -b 0.0.0.0
#*sudo apt install nginx
#*systemctl status nginx
#*sudo nano /etc/nginx/sites-enabled/default
#*location / {
#*        proxy_pass http://127.0.0.1:8000;
#*        proxy_set_header Host $host;
#*        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#*    }
#*gunicorn "urlshort:create_app()" -b 0.0.0.0 --daemon