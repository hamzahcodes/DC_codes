# import socket
# import threading

# host = socket.gethostbyname(socket.gethostname())
# port = 5051

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((host, port))
# server.listen()

# clients = []
# nicknames = []

# def broadcast(message):
#     for client in clients:
#         client.send(message)

# def handle_client(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             broadcast(message)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             broadcast(f'{nickname} left the chat!'.encode('ascii'))
#             nicknames.remove(nickname)
#             break

# def receive():
#     while True:
#         client, address = server.accept()
#         print(f'Connected with {str(address)}')

#         client.send('NICK'.encode('ascii'))
#         nickname = client.recv(1024).decode('ascii')
#         nicknames.append(nickname)
#         clients.append(client)

#         print(f'Nickname of the client is {nickname}')
#         broadcast(f'{nickname} joined the chat'.encode('ascii'))
#         client.send('Connected to server'.encode('ascii'))

#         thread = threading.Thread(target=handle_client, args=(client, ))
#         thread.start()


# print('Server is Listening ...')
# receive()


import socket
import struct

multicast_group = '224.3.29.71'
server_address = ('', 5009)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    msg, address = sock.recvfrom(1024)
    print("Recieved from",address, ": ", msg.decode())
