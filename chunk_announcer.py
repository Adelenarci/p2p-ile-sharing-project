import time
import socket
import os
import json

broadcast_address = "255.255.255.255"
broadcast_port = 5001
directory_path = "/Users/akk/Desktop/Code/pythonProject/"

def get_file_names():
    try:
        file_names = os.listdir(directory_path)
        print(f"File names in the directory: {file_names}")
        return file_names
    except Exception as e:
        print(f"Error occurred while reading the directory: {e}")

def broadcast_file_names(file_names):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        try:
            message = json.dumps({"chunks": file_names})
            sock.sendto(message.encode(), (broadcast_address, broadcast_port))
            print(f"Broadcast message sent: {message}")
            time.sleep(60)

        except Exception as e:
            print(f"Error occurred while broadcasting: {e}")

if __name__ == "__main__":
    file_names = get_file_names()
    broadcast_file_names(file_names)
