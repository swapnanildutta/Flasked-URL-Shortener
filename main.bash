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
