# src/chat.py

import os

CHATLOG_PATH = '../data/chatlog.txt'

def read_chat():
    if os.path.exists(CHATLOG_PATH):
        with open(CHATLOG_PATH, 'r') as file:
            chat_data = file.readlines()
    else:
        chat_data = []
    return [message.strip() for message in chat_data]

def write_chat(message):
    with open(CHATLOG_PATH, 'a') as file:
        file.write(message + '\n')
