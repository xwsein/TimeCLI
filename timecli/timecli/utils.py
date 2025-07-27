import os
import json
from datetime import datetime

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def load_json(path):
    if not os.path.exists(path):
        ensure_dir(path)
        with open(path, 'w') as f:
            json.dump([], f)
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    ensure_dir(path)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def timestamp_now():
    return datetime.now().isoformat()

