from server import receive
from client import send
from configparser import ConfigParser


config = ConfigParser()
config.read('ips.ini')
this_pc = config.get("IPS", "this_pc_ip")
another_pc = config.get("IPS", "another_computer_ip")
PORT = 38357
mode = input("Choose mode : send - send message , receive - receive message : ")
if mode == "send":
    message = input("Input your message : ")
    print(send(another_pc, PORT, message))
elif mode == "receive":
    print(receive(this_pc, PORT))
else:
    print("Incorrect mode !")
