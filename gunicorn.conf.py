# /home/ubuntu/Python-Static-website/gunicorn.conf.py

import multiprocessing

# Bind to a Unix socket for Nginx <-> Gunicorn communication
bind = "unix:/home/ubuntu/Python_Static_website/gunicorn.sock"

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
threads = 2

# App settings
chdir = "/home/ubuntu/Python_Static_website"
wsgi_app = "Python_Static_website.wsgi:application"  # Django WSGI entry point

# Logging
accesslog = "/home/ubuntu/Python_Static_website/logs/gunicorn-access.log"
errorlog = "/home/ubuntu/Python_Static_website/logs/gunicorn-error.log"
loglevel = "info"

# Daemonization (let systemd handle this, so keep False)
daemon = False

# Security limits
limit_request_line = 4094
limit_request_fields = 100
