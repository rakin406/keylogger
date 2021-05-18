# keylogger

Key logging program for *ethical* hacking purposes.

## Installation

```shell
git clone https://github.com/rakin406/keylogger.git
cd keylogger
pip3 install pynput
```

## Usage

You can start the server in two ways, one is using server.py and the other is
netcat utility.

```shell
./server.py
./client.py localhost
```

```shell
nc -l -k 1234
./client.py localhost
```
