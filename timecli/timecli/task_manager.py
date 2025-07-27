### task_manager.py
from datetime import datetime, timedelta
from .storage import load_data, save_data
from .notifier import notify

def add_task(title, due=None):
    data = load_data()
    task_id = len(data.get("tasks", [])) + 1
    task = {"id": task_id, "title": title, "created": str(datetime.now())}
    if due:
        task["due"] = due
    data.setdefault("tasks", []).append(task)
    save_data(data)
    print(f"✅ Task added: [{task_id}] {title}")

def edit_task(task_id, title=None, due=None):
    data = load_data()
    for task in data.get("tasks", []):
        if task["id"] == task_id:
            if title:
                task["title"] = title
            if due:
                task["due"] = due
            save_data(data)
            print(f"✏️ Task [{task_id}] updated")
            return
    print("❌ Task not found")

def delete_task(task_id):
    data = load_data()
    tasks = data.get("tasks", [])
    tasks = [t for t in tasks if t["id"] != task_id]
    data["tasks"] = tasks
    save_data(data)
    print(f"🗑️ Task [{task_id}] deleted")

def list_tasks():
    data = load_data()
    tasks = data.get("tasks", [])
    print("📋 Tasks:")
    for task in tasks:
        print(f"[{task['id']}] {task['title']}")
        if 'due' in task:
            print(f"  ⏳ Due: {task['due']}")
        print(f"  🕒 Created: {task['created']}")

def schedule_day(start_time, date, title_duration):
    if len(title_duration) % 2 != 0:
        print("❌ Provide pairs of task and duration (in minutes)")
        return

    current = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
    for i in range(0, len(title_duration), 2):
        title = title_duration[i]
        duration = int(title_duration[i + 1])
        end = current + timedelta(minutes=duration)
        due_str = end.strftime("%Y-%m-%d %H:%M")
        add_task(title, due_str)
        notify("📌 Task Start", f"{title} starting at {current.strftime('%H:%M')}")
        notify("✅ Task End", f"{title} ends at {end.strftime('%H:%M')}")
        current = end
