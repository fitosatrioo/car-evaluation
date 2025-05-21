bind = "0.0.0.0:$PORT"  # Use environment variable PORT
workers = 4  # Number of worker processes
worker_class = "sync"
timeout = 120
keepalive = 5
# Logging configuration
errorlog = "-"  # stderr
accesslog = "-"  # stdout
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'