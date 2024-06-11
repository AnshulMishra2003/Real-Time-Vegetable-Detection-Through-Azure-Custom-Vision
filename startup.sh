#!/bin/bash

# Update package lists
apt-get update

# Install the necessary dependencies
apt-get install -y libjpeg-dev

# Run the gunicorn server
gunicorn --bind 0.0.0.0:8000 app:app
