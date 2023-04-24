processes = int(input("Enter no. of processes: "))

print(f"Process with id {processes - 1} fails")

start = int(input("Enter the process who starts the election: "))
for j in range(start, processes):
    if j == processes - 1:
        break
    for i in range(j + 1, processes):
        if i == processes - 1:
            break
        print(f"Election message sent by Process {j} to Process {i}")
    for i in range(j + 1, processes):
        if i == processes - 1:
            break
        print(f"Ok message sent by Process {i} to Process {j}")

print(f"process {processes - 2} is now the leader")

j = processes
for i in range(processes - 1) :
    if i == processes - 2:
        break
    print(f"Process with id {processes - 2} sends co-ordinator message to process {processes - j}")
    j -= 1