### storage.py
import json
import os

FILE = "timecli_data.json"

def load_data():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)


### timer.py
import time
from .notifier import notify

def start_pomodoro(title, work=25, break_time=5, rounds=4):
    for i in range(rounds):
        print(f"🍅 Pomodoro {i+1}/{rounds}: {title} - Work {work} min")
        notify("Pomodoro Start", f"Session {i+1}: {title}")
        time.sleep(work * 60)

        print(f"☕ Break {break_time} min")
        notify("Pomodoro Break", f"Break after session {i+1}")
        time.sleep(break_time * 60)

    print("🎉 Pomodoro complete!")
    notify("Pomodoro Done", "All sessions completed")

