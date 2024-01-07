#!/bin/bash

set -ex

python manage.py wait_for_db
# python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py create_superuser
python manage.py create_initial_db_content
python manage.py runserver 0.0.0.0:8000