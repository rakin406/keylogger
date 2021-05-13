#!/usr/bin/env python3
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen()
addr = ""

while True:
    client, address = server.accept()

    # Print address only once
    if addr == "":
        addr = address
        print(f"Connection from {addr} has been made.")

    msg = client.recv(64).decode("utf-8")
    print(msg)
