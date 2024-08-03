# src/app.py
from flask import Flask, request, jsonify
import os
from chat import read_chat, write_chat

app = Flask(__name__)
chat_file_path = 'data/chatlog.txt'

@app.route('/chat', methods=['GET'])
def get_chat():
    if not os.path.exists(chat_file_path):
        return jsonify({"error": "Chat log not found"}), 404
    chat_data = read_chat()
    return jsonify({"chat": chat_data})

@app.route('/chat', methods=['POST'])
def post_chat():
    message = request.form.get('message')
    if not message:
        return jsonify({"error": "No message provided"}), 400
    write_chat(message)
    return jsonify({"success": "Message added"}), 200

if __name__ == "__main__":
    app.run(debug=True)
