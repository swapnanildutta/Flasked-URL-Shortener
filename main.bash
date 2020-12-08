#!/bin/bash
#*pip3 install pipenv
#*pipenv install
pipenv shell
#*pipenv install flask
export FLASK_APP=hello
flask run
export FLASK_ENV=development