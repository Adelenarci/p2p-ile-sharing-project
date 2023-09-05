import socket
import json
import os

listening_port = 5000
directory_path = "/Users/akk/Desktop/Code/pythonProject/"

def handle_requests():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", listening_port))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        print(f"Received connection from {addr}")
        handle_connection(conn)

def handle_connection(conn):
    data = conn.recv(1024).decode()
    request = json.loads(data)
    print(f"Received request: {request}")

    if "requested content" in request:
        send_file(conn, request["requested content"])

def send_file(conn, file_name):
    try:
        with open(os.path.join(directory_path, file_name), "rb") as file:
            data = file.read()
            conn.send(data)
            print(f"Sent file: {file_name}")
    except Exception as e:
        print(f"Error occurred while sending file: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    handle_requests()