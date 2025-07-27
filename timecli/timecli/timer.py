import time
from win10toast import ToastNotifier

toaster = ToastNotifier()


def _notify(title, msg):
    toaster.show_toast(title, msg, duration=10, threaded=True)


def _countdown(minutes, label):
    total_seconds = int(minutes * 60)
    try:
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            print(f"{label} ⏳ {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
        print(" " * 30, end="\r")  # clear line
    except KeyboardInterrupt:
        print("\n⏹️  Timer interrupted.")
        return False
    return True


def start_pomodoro(title, work=25, break_time=5, rounds=4):
    print(f"🍅 Starting Pomodoro: {title}")
    for i in range(1, rounds + 1):
        print(f"\n🔁 Round {i}/{rounds} - Work Time")
        _notify("Pomodoro Started", f"{title} - Round {i} Work")
        if not _countdown(work, "Work"):
            break

        if i < rounds:
            print(f"\n☕ Break Time")
            _notify("Break Time", f"{title} - Round {i} Break")
            if not _countdown(break_time, "Break"):
                break
    print("\n✅ Pomodoro session complete!")
    _notify("Done!", f"{title} session completed.")
