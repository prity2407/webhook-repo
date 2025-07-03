from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.github_webhooks

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event = request.headers.get('X-GitHub-Event')
    timestamp = datetime.utcnow()

    entry = {
        "action_type": event,
        "author": data.get('sender', {}).get('login'),
        "timestamp": timestamp,
    }

    if event == "push":
        entry["to_branch"] = data.get('ref', '').split('/')[-1]
    elif event == "pull_request":
        pr = data.get('pull_request', {})
        entry["from_branch"] = pr.get('head', {}).get('ref')
        entry["to_branch"] = pr.get('base', {}).get('ref')

    db.events.insert_one(entry)
    return jsonify({"status": "success"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    events = list(db.events.find().sort("timestamp", -1).limit(10))
    for e in events:
        e['_id'] = str(e['_id'])  # MongoDB ID to string
        e['timestamp'] = e['timestamp'].strftime("%d %B %Y - %I:%M %p UTC")
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
