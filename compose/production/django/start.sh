#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
uvicorn dal.asgi:application --work 12 --chdir=/app