import socket
import threading

def handle_client(client_socket, addr):
    print(f"Connected: {addr}")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print(f"Disconnected: {addr}")
                break
            print(f"Received from {addr}: {message}")
            broadcast(message)
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except Exception as e:
            print(f"Error broadcasting message: {e}")

HOST = '0.0.0.0'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Server listening on {HOST}:{PORT}")

clients = []

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()
