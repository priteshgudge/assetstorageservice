#!/bin/bash
sleep 5s

echo "############# Running assetstorage using unicorn ################"
gunicorn -c assetstorageservice/conf/gunicorn.py assetstorageservice.conf.service_app:app

