from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHATLOG_PATH = os.path.join(BASE_DIR, 'data', 'chatlog.txt')

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/chat', methods=['POST'])
def add_message():
    message = request.form['message']
    with open(CHATLOG_PATH, 'a') as file:
        file.write(message + '\n')
    return jsonify(success=True)

@app.route('/chatlog', methods=['GET'])
def get_chatlog():
    if os.path.exists(CHATLOG_PATH):
        with open(CHATLOG_PATH, 'r') as file:
            chat_data = file.readlines()
    else:
        chat_data = []
    return jsonify(chat=chat_data)

if __name__ == '__main__':
    app.run(debug=True)