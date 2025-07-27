import os
import shutil
import sys
import winreg

def add_to_path():
    exe_path = os.path.abspath(sys.argv[0])
    target_dir = os.path.dirname(exe_path)

    # Add target_dir to user PATH
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_SET_VALUE,
    )
    try:
        path, _ = winreg.QueryValueEx(key, "Path")
        if target_dir not in path:
            new_path = path + ";" + target_dir
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
            print(f"✅ Added {target_dir} to PATH. Restart terminal to use `timecli`.")
        else:
            print(f"ℹ️ {target_dir} already in PATH.")
    except FileNotFoundError:
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, target_dir)
        print(f"✅ Set new PATH with {target_dir}.")
    winreg.CloseKey(key)

if __name__ == "__main__":
    add_to_path()