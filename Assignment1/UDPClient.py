from socket import *

server_address = ('127.0.0.1', 12000)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

ping_message = "Ping"
num_pings = 10
ping_attempt = 1

for ping in range(num_pings):
    message_to_send = f"{ping_message} {ping_attempt}"
    try:
        client_socket.sendto(message_to_send.encode(), server_address)
        print("Ping sent")

        response, server_address = client_socket.recvfrom(1024)
        print(f"Received from {server_address}: {response.decode().upper()}")

    except:
        print("Request timed out")
    ping_attempt += 1


client_socket.close()