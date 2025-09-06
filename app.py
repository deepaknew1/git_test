##This whole dir/ folder has been pused in my git branch 
import time
import redis
from flask import Flask

app= Flask(__name__)
cache=redis.Redis(host='redis',port=6379)

def get_hit_count():
    retries=5
    while True:
        try:
            #cache.reset_retry_count()
            return cache.incr('this')
        except redis.exceptions.connectionError as exc:
            if retries==0:
                raise exc
            retries=-1
            time.sleep(1)

@app.route('/')
def hello():
    count=get_hit_count()
    return 'Hello deepak! I have been seen {} times. \n'.format(count)
