import socket

host = socket.gethostbyname(socket.gethostname())
port = 5052

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

msg = input("Message: ")

while msg != 'bye':
    client.send(msg.encode('utf-8'))    
    msg = client.recv(1024).decode('utf-8')
    print("Server: ", str(msg))

    msg = input("Message: ")

client.close()