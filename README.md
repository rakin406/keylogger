# Keylogger

This is a keylogger written in Python. There are two ways of running it: executing `main.py` 
or through a socket connection using `server.py` and `client.py`.

When `main.py` is executed, it monitors keypresses and saves them to a file named `keys.txt` 
in the current working directory. Every 30 minutes, the program sends an email with the 
file attached.

**[Demo](https://vimeo.com/1176095621?fl=ip&fe=ec)**

## Environment Variables

To run `main.py`, you will need to add the following environment variables to your .env file.

`RESEND_API_KEY`
`EMAIL`

## Prerequisites

Before you begin, ensure you have the following installed and configured:

*   **Python**

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/rakin406/keylogger.git
    cd keylogger
    ```

2.  Install project dependencies:
    ```bash
    pip install pynput python-dotenv resend
    ```

## Usage

To run the keylogger, execute the `main.py` script.
```bash
python main.py
```

If you want to use the socket version instead, run `server.py` and then `client.py`. 
These two commands must be executed in separate terminals.
```bash
python server.py
```
```bash
python client.py localhost
```

If you have netcat installed, you can use it instead of running `server.py`.
```bash
nc -l -k 1234
```

Server will print the keys pressed by the client.

## Contact

Rakin Rahman - rakinrahman406@gmail.com

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
