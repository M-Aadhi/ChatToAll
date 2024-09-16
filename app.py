from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__)

CHATLOG_PATH = 'data/chatlog.json'

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/chat', methods=['POST'])
def add_message():
    message = request.form['message']
    if os.path.exists(CHATLOG_PATH):
        with open(CHATLOG_PATH, 'r') as file:
            chat_data = json.load(file)
    else:
        chat_data = []
    chat_data.append({"message": message})
    with open(CHATLOG_PATH, 'w') as file:
        json.dump(chat_data, file, indent=4)
    return jsonify(success=True)

@app.route('/chatlog', methods=['GET'])
def get_chatlog():
    if os.path.exists(CHATLOG_PATH):
        with open(CHATLOG_PATH, 'r') as file:
            chat_data = json.load(file)
    else:
        chat_data = []
    return jsonify(chat=[entry['message'] for entry in chat_data])

if __name__ == '__main__':
    app.run(debug=True)