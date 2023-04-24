import socket

host = socket.gethostbyname(socket.gethostname())
port = 5052

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()
print('[SERVER IS LISTENING]')

client, addr = server.accept()
print(f'New connection from {addr}', '\n')

while True:
    msg = client.recv(1024).decode('utf-8')
    if not msg:
        break
    print("Client: " + str(msg))

    send_msg = input(">: ")
    client.send(send_msg.encode('utf-8'))