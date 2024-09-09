# src/chat.py

import os

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHATLOG_PATH = os.path.join(BASE_DIR, 'data', 'chatlog.txt')

def read_chat():
    if os.path.exists(CHATLOG_PATH):
        with open(CHATLOG_PATH, 'r') as file:
            chat_data = file.read()
        return chat_data
    return ""

def write_chat(message):
    with open(CHATLOG_PATH, 'a') as file:
        file.write(message + '\n')