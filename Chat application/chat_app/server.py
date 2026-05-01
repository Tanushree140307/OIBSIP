import socket

host = '127.0.0.1'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print("Waiting for connection...")
conn, addr = server.accept()
print("Connected to", addr)

while True:
    message = conn.recv(1024).decode()
    print("Client:", message)

    reply = input("You: ")
    conn.send(reply.encode())