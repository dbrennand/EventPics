#!/bin/bash

# Run PostgreSQL database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create the superuser
python manage.py createsuperuser --noinput

# Get the number of workers from the environment variable, default to 2 if not set
WORKERS=${EVENTPICS_WSGI_WORKERS:-2}

# Start the web server
gunicorn --bind :8000 --workers ${WORKERS} eventpics.wsgi
