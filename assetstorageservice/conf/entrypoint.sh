#!/bin/bash
sleep 5s

echo "############# Running assetstorage using unicorn ################"
gunicorn -c gunicorn.py service_app:app

