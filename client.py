import sys
import threading
import time
import socket
import os
from pyfiglet import Figlet

os.system("clear")
pyf = Figlet(font='puffy')
a = pyf.renderText("UDP Chat Pemrograman Jaringan")
os.system("tput setaf 3")
print(a)

HOST = "127.0.0.1"  # Jangan dirubah
PORT = 8081  # Jangan dirubah
SERVER_HOST = "165.22.251.42"  # Dirubah sesuai IP Server
SERVER_PORT = 8072  # Jangan dirubah

print("Initializing....")
name = input("Enter your name: ")


print("Waiting to connect....")
time.sleep(1)
print("Connection established....")


def receiver():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind((HOST, PORT))
    while True:
        msg = client.recvfrom(1024)
        message = msg[0].decode()
        username = message.split(':')[0]
        if name != username:
            print(message)


# Function for sending
def sender():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((SERVER_HOST, SERVER_PORT))
    text = "hello"
    while True:
        if "bye" in text or "exit" in text or "finish" in text:
            exit()
        else:
            text = input(f'{name}:')
            text = name+":"+text
            client.sendto(text.encode(), (SERVER_HOST, SERVER_PORT))


# Using Multi-threading
send = threading.Thread(target=sender)
receive = threading.Thread(target=receiver)

send.start()
receive.start()
