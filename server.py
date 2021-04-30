#!/usr/bin/env python3
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen()

while True:
    client, address = server.accept()
    print(f"Connection from {address} has been made.")
    msg = client.recv(64).decode("utf-8")
    print(msg)
