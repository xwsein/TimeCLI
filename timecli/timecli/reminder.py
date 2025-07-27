### reminder.py
from datetime import datetime, timedelta
import threading
import time
from .notifier import notify

def set_reminder(message, at):
    if at.lower() == "now":
        notify("🔔 Reminder", message)
        return

    try:
        now = datetime.now()
        target = datetime.strptime(at, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
        if target < now:
            target += timedelta(days=1)

        delay = (target - now).total_seconds()

        def reminder_thread():
            time.sleep(delay)
            notify("🔔 Reminder", message)

        threading.Thread(target=reminder_thread, daemon=True).start()
        print(f"⏰ Reminder set for {target.strftime('%H:%M')}")
    except ValueError:
        print("❌ Invalid time format. Use HH:MM (24-hour) or 'now'.")


### notifier.py
from plyer import notification

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="timecli",
        timeout=10
    )
