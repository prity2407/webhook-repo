# GitHub Webhook Receiver

This repository contains a Flask-based application that listens for GitHub webhook events (Push) from a separate GitHub repository (`action-repo`), stores them in a MongoDB database, and displays the latest activity on a simple UI.

---

## 🔧 Features

- ✅ Receives real-time **push events** via GitHub Webhooks
- ✅ Stores events in **MongoDB**
- ✅ Live front-end that auto-refreshes every 15 seconds
- ✅ Displays: username, branch, timestamp
- 🔄 Easily extensible to support Pull Requests & Merge events

---

## 🛠 Tech Stack

- **Backend**: Python (Flask)
- **Database**: MongoDB
- **Frontend**: HTML, CSS, JavaScript
- **Dev Tools**: ngrok, GitHub Webhooks

---

## 📦 Folder Structure

webhook-repo/
├── app.py # Flask backend server
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend UI
└── static/
└── script.js # AJAX polling logic


---

## 🚀 How to Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt

2. Start MongoDB

Make sure MongoDB is running locally:

mongod

3. Start Flask App

python app.py

4. Start ngrok (to expose port 5000)

ngrok http 5000


5. Set Up GitHub Webhook

    Go to your action-repo on GitHub

    Navigate to: Settings → Webhooks → Add Webhook

    Payload URL: https://<your-ngrok-url>/webhook

    Content Type: application/json

    Event Type: Just the push event

✅ Sample UI Output

"prity2407" pushed to "main" on 3 July 2025 - 07:22 PM UTC




🧑‍💻 Author

Preety Sriwastava
GitHub
