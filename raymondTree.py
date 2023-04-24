n = 5

holder = {0:0, 1:0, 2:0, 3:1, 4:1}
token = {0:1, 1:0, 2:0, 3:0, 4:0}
request_queue = {0:[], 1:[], 2:[], 3:[], 4:[]}

adj_matrix = [[1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,1,0,0,0]]

print("Raymond Tree based Mutual Exclusion")
print("\nAdjacency Matrix for the spanning tree:\n")

for i in adj_matrix:
    print(*i)

req_process = int(input("Enter the process who want to enter CS: "))

def find_parent(req_process):
    request_queue[req_process].append(req_process)
    for i in range(n):
        if adj_matrix[req_process][i] == 1:
            parent = i
            request_queue[parent].append(req_process)
            break
    
    print(f"Process {req_process} sending request to {parent} process")
    print(f"request queue : {request_queue}")

    if token[parent] == 1:
        return parent
    
    else:
        parent = find_parent(parent)

    return parent

parent = find_parent(req_process)

while token[req_process] != 1:
    child = request_queue[parent][0]
    request_queue[parent].pop(0)
    holder[parent] = child
    holder[child] = 0
    token[parent] = 0
    token[child] = 1
    print(f"Parent process {parent} has the token and sends it to child {child}")
    parent = child

if token[parent] == 1 and request_queue[parent][0] == parent:
    request_queue[parent].pop(0)
    holder[parent] = parent
    print(f"Process {parent} enters critical section")

if (not len(request_queue[parent])):
    print(f"request queue of parent is empty. Hence releasing CS")

print("\nHolder", holder)