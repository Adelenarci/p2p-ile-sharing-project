import socket
import json

listening_port = 5001
content_dictionary = {}

def listen_for_broadcasts():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", listening_port))

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received broadcast from {addr}: {data.decode()}")
        update_content_dictionary(data.decode(), addr[0])

def update_content_dictionary(message, ip):
    data = json.loads(message)
    for file_name in data["chunks"]:
        if file_name not in content_dictionary:
            content_dictionary[file_name] = []
        content_dictionary[file_name].append(ip)
    print(f"Updated content dictionary: {content_dictionary}")

if __name__ == "__main__":
    listen_for_broadcasts()
