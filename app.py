from flask import Flask, render_template, request, jsonify
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    count = redis.get('hits')
    return render_template('frontend/index.html', count=int(count) if count else 0)

@app.route('/get', methods=['GET'])
def get_count():
    count = redis.get('hits')
    return jsonify({'count': int(count) if count else 0})

@app.route('/incr', methods=['POST'])
def increase():
    redis.incr('hits')
    count = redis.get('hits')
    return jsonify({'count': int(count) if count else 0})

@app.route('/decr', methods=['POST'])
def decrease():
    redis.decr('hits')
    count = redis.get('hits')
    return jsonify({'count': int(count) if count else 0})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

