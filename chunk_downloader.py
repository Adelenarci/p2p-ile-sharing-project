import socket
import json
import time

content_dictionary_path = "/Users/akk/Desktop/Code/pythonProject/content_dictionary.json"

def download_file():
    file_name = input("Enter the name of the file you want to download: ")
    print(f"Attempting to download file: {file_name}")

    for i in range(1, 6):
        chunk_name = f"{file_name} {i}"
        download_chunk(chunk_name)

def download_chunk(chunk_name):
    try:
        with open(content_dictionary_path, "r") as file:
            content_dictionary = json.load(file)
    except Exception as e:
        print(f"Error occurred while reading content dictionary: {e}")
        return

    if chunk_name not in content_dictionary:
        print(f"Chunk {chunk_name} is not available.")
        return

    for ip in content_dictionary[chunk_name]:
        if send_request(chunk_name, ip):
            break

def send_request(chunk_name, ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, 5000))
        message = json.dumps({"requested content": chunk_name})
        sock.send(message.encode())
        print(f"Sent request for {chunk_name} to {ip}")


        with open(chunk_name, 'wb') as file:
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                file.write(data)
            print(f"Downloaded {chunk_name} from {ip}")

        return True
    except Exception as e:
        print(f"Error occurred while sending request to {ip}: {e}")
        return False
    finally:
        sock.close()

if __name__ == "__main__":
    while True:
        download_file()
        time.sleep(60)
