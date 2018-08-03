import os


def numCPUs():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")


bind = "0.0.0.0:7500"
workers = numCPUs() * 2 + 1
backlog = 2048
worker_class ="gevent"
debug = True
daemon = False
pidfile ="/tmp/assetstorage-gunicorn.pid"
logfile ="/tmp/assetstorage-gunicorn.log"
loglevel = 'info'
accesslog = '/tmp/gunicorn-access.log'
timeout = 120
