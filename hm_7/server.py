from socket import socket, SOL_SOCKET, SO_REUSEADDR


def receive(host, port):
    with socket() as s:
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        connection, address = s.accept()
        print(f"Connected from {address}")
        data = connection.recv(256)
        connection.send(b"OK")
        connection.close()
    return f"Received a new incoming message : {data.decode('UTF-8')}"
