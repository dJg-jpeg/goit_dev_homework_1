from socket import socket


def send(host, port, message):
    with socket() as s:
        try:
            s.connect((host, port))
            s.send(message.encode("UTF-8"))
            data = s.recv(16)
            if data.decode("UTF-8") == "OK":
                return "Your message was successfully received"
        except (ConnectionRefusedError, ConnectionError, ConnectionResetError, ConnectionAbortedError, TimeoutError):
            return "Something went wrong , please try again"
