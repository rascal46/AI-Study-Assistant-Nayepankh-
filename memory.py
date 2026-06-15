import json
import os

FILE_NAME = "memory.json"

def load_memory():

    if not os.path.exists(FILE_NAME):
        return {
            "topics": [],
            "chat_history": []
        }

    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_memory(data):

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)