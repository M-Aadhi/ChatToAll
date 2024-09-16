# src/chat.py

import json
import os

CHATLOG_PATH = '../data/chatlog.json'

def read_chat():
    if os.path.exists(CHATLOG_PATH):
        with open(CHATLOG_PATH, 'r') as file:
            chat_data = json.load(file)
    else:
        chat_data = []
    return chat_data

def write_chat(message):
    chat_data = read_chat()
    chat_data.append({"message": message})
    with open(CHATLOG_PATH, 'w') as file:
        json.dump(chat_data, file, indent=4)
