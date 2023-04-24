import math

server_time = str(input("Enter server time: "))
server_time = int(server_time[:1]) * 60 + int(server_time[2:4])

num_clients = int(input("Enter no. of clients: "))

clients = []
for i in range(num_clients):
    clients.append(input(f"Enter time of server no. {i + 1}: "))

diff = 0
offset = []
for client_time in clients:
    ct = int(client_time[:1]) * 60 + int(client_time[2:4])
    diff += (ct - server_time)
    offset.append(ct - server_time)

print(offset)
print(diff)
print(num_clients)
adjusted_time = int(diff / (num_clients + 1))
server_time += adjusted_time
print(server_time)
final_time = f'{math.floor(server_time / 60)}:{server_time % 60}'
print(final_time)

print(f'Server will have to adjust its time by {adjusted_time} minutes')
i = 1
for i in range(num_clients):
    print(f"Client {i + 1} will have to adjust by {(server_time % 60) - offset[i]} minutes")
