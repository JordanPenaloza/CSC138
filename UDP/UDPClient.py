from socket import *

serverName = 'localhost' # 127.0.0.1
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Please enter your message in lowercase format: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
print("Upper case message: ", modifiedMessage.decode())

clientSocket.close() 