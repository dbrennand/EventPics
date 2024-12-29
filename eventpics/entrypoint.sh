#!/bin/sh

# Run PostgreSQL database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create the superuser
python manage.py createsuperuser --noinput

# Start the web server
gunicorn --bind :8000 --workers 2 eventpics.wsgi
