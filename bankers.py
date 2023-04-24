processes = int(input("Enter no of processes: "))
resources = int(input("Enter no. of resources: "))

print(f"\nEnter allocated resources for each process : \n")

allocated = []
for i in range(processes):
    lst = []
    s = input(f"Process {i+1} : ")
    for j in s.split():
        lst.append(int(j))
    allocated.append(lst)
    
print(f"\nEnter maximum resources for each process : \n")
max_need = []
for i in range(processes):
    lst = []
    s = input(f"Process {i + 1}: ")
    for j in s.split():
        lst.append(int(j))
    max_need.append(lst)

print(max_need)

print(f"\nEnter available resources : \n")
available = []
for i in input().split():
    available.append(int(i))

print(available)

safe_sequence = []
visited = [0] * processes

def can_allocate_resources(i):
    for j in range(resources):
        if max_need[i][j] - allocated[i][j] > available[j]:
            return False
    return True

def release_resources(i):
    for j in range(resources):
        available[j] += allocated[i][j]
    visited[i] = 1
    safe_sequence.append(i)

while visited.count(0) != 0:
    not_found = True
    for i in range(processes):
        if visited[i] == 0 and can_allocate_resources(i) == True:
            release_resources(i)
            not_found = False
        
    if not_found == False:
        break

if len(safe_sequence) == processes:
    print(f"\nThe processes are in safe state and the safe sequence is : {safe_sequence}")
else:
    print("\nThe processes are in an unsafe state")