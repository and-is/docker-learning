from flask import Flask
from redis import Redis,RedisError
import os
import socket

redis = Redis(host="redis", db=0, socker_connect_timeout=2, socket_timeout=2)

app = Flash(__name__)

@app.route("/")

def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Can't connect to Redis!!!</i>"
    
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname: </b> {hostname}<br/>" \
           "<b>Visits: </b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socker.gethostname(), visit=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80) 