"""If you want to start messaging with a server on your pc , please run this file"""
from socket import socket, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from configparser import ConfigParser
from client import user_interface


def message_server(host, server_port, clients_ips):
    answers = {clients_ips[0]: '',
               clients_ips[1]: '',
               }
    with socket() as s:
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((host, server_port))
        s.listen(2)
        while True:
            conn, addr = s.accept()
            ip = addr[0]
            data = conn.recv(256)
            answers[ip] = data
            for this_ip, this_answer in answers.items():
                if this_ip == ip:
                    continue
                elif len(this_answer) == 0:
                    break
                conn.send(this_answer)
                answers[this_ip] = ''
            conn.close()


if __name__ == "__main__":
    config = ConfigParser()
    config.read('ips.ini')
    this_pc = config.get("IPS", "this_pc_ip")
    another_pc = config.get("IPS", "another_computer_ip")
    port = int(config.get("IPS", "port"))
    print("Print exit to exit the app...\n\n\n")
    server = Thread(target=message_server, args=(this_pc, port, (this_pc, another_pc)))
    server.start()
    user_me = Thread(target=user_interface, args=(this_pc, port))
    user_me.start()
