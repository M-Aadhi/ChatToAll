# src/chat.py

def read_chat():
    with open('../data/chatlog.txt', 'r') as file:
        chat_data = file.read()
    return chat_data

def write_chat(message):
    with open('../data/chatlog.txt', 'a') as file:
        file.write(message + '\n')
