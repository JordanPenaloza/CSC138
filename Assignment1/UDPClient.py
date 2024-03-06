from socket import *
import time

server_address = ('127.0.0.1', 12000)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

ping_message = "Ping"
num_pings = 10
ping_attempt = 1

def calculateRTT(end_time, start_time):
    return (end_time - start_time) * 1000

for ping in range(num_pings):

    start_time = time.time()
    message_to_send = f"{ping_message} {ping_attempt}"
    client_socket.sendto(message_to_send.encode(), server_address)
    print("Ping sent")

    try:
        response, server_address = client_socket.recvfrom(1024)
        print(f"Received from {server_address}: {response.decode().upper()}")

        end_time = time.time()
        rtt = calculateRTT(end_time, start_time)
        print(f"RTT: {rtt}")

    except:
        print("Request timed out")
    ping_attempt += 1

client_socket.close()