from socket import *
import random

#simulates artificial packet loss if rand is less than 4
#capitalizes messages received from the client and sends them back

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',12000))

while True:
    rand = random.randint(0,10)
    message, address = serverSocket.recvfrom(1024)
    message = message.decode().upper()
    if rand < 4:
        continue
    else:
        serverSocket.sendto(message.encode(), address)
        print("Encoded and sent message")
