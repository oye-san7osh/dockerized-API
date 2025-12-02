#!/bin/bash

set -e

echo "Starting Django Application..."

# Apply Database Migrations
python manage.py migrate

exec "$@"
