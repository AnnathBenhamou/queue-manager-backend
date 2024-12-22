from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from queue import Queue, Empty
import threading

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

queues = {}
queues_lock = threading.Lock()

def get_or_create_queue(queue_name):
    with queues_lock:
        if queue_name not in queues:
            queues[queue_name] = Queue()
        return queues[queue_name]

@app.route('/api/<queue_name>', methods=['POST'])
def add_message(queue_name):
    message = request.get_json()
    if not message:
        return jsonify({"error": "Invalid JSON payload"}), 400

    queue = get_or_create_queue(queue_name)
    queue.put(message)
    return jsonify({"status": "Message added to queue"}), 200

@app.route('/api/<queue_name>', methods=['GET'])
def get_message(queue_name):
    timeout = request.args.get('timeout', default=10, type=int)
    queue = get_or_create_queue(queue_name)

    try:
        message = queue.get(timeout=timeout)
        return jsonify(message), 200
    except Empty:
        return '', 204

@app.route('/queues', methods=['GET'])
def list_queues():
    with queues_lock:
        queue_info = {name: q.qsize() for name, q in queues.items()}
    return jsonify(queue_info), 200

if __name__ == '__main__':
    app.run(debug=True)
