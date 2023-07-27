from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    redis_client.incr('visits')
    visits = redis_client.get('visits')
    return f'방문 횟수: {visits}회'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
