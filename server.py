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

HOST = "127.0.0.1"
PORT = 8072
CLIENT_PORT = 8081
clients = []
# AF_INET = Network Address Family : IPv4
# SOCK_DGRAM = DataGram Socket : UDP


def receiver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))  # binding the IP address and port number
    while True:
        msg = s.recvfrom(1024)
        message = msg[0].decode()

        # Get address
        address = msg[1]

        username = message.split(':')[0]

        print(username + ' is connected !')
        # Mencari apakah ip address client sudah terdaftar
        if address not in clients:
            clients.append(address)

        if "exit" in message or "bye" in message:
            index = clients.index(address)
            clients.remove(index)

        broadcast(s, message)

# Function for sending


def broadcast(s, message):
    if len(clients) > 0:
        for client in clients:
            s.sendto(message.encode(), (client[0], CLIENT_PORT))


print("Waiting for client....")

# Using Multi-threading
receive = threading.Thread(target=receiver)

receive.start()
