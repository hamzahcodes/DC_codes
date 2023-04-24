# import socket
# import threading

# nickname = input("Enter a nickname: ")
# host = socket.gethostbyname(socket.gethostname())
# port = 5051

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((host, port))

# def receive():
#     while True:
#         try:
#             message = client.recv(1024).decode('ascii')
#             if message == 'NICK':
#                 client.send(nickname.encode('ascii'))
#             else:
#                 print(message)

#         except:
#             print('An error occured')
#             client.close()
#             break

# def write():
#     while True:
#         message = f'{nickname}: {input("")}'
#         if message == 'quit':
#             client.close()
#             break
#         client.send(message.encode('ascii'))
    
# recieve_thread = threading.Thread(target=receive)
# recieve_thread.start()
# write_thread = threading.Thread(target=write)
# write_thread.start()

import socket

multicast_group = ('224.3.29.71', 5009)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

message = "This is client message"

client.sendto(message.encode(), multicast_group)
