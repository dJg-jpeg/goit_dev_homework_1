"""If you want to start messaging with connection to another PC , please run this file"""
from socket import socket
from configparser import ConfigParser


def send(server_ip, server_port, message):
    with socket() as s:
        try:
            s.connect((server_ip, server_port))
            s.send(message.encode("UTF-8"))
            data = s.recv(256)
            if data:
                print(f"|Another PC| : {data.decode('UTF-8')}")
        except (ConnectionRefusedError, ConnectionError, ConnectionResetError, ConnectionAbortedError, TimeoutError):
            print(f"//Something went wrong , please try again//")


def user_interface(server_ip, server_port):
    while True:
        message = input("|Me| : ")
        if message == "exit":
            send(server_ip, server_port, message)


if __name__ == "__main__":
    config = ConfigParser()
    config.read('ips.ini')
    this_pc = config.get("IPS", "this_pc_ip")
    another_pc = config.get("IPS", "another_computer_ip")
    port = int(config.get("IPS", "port"))
    print("Print exit to exit the app...\n\n\n")
    user_interface(another_pc, port)
