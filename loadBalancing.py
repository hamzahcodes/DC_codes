servers = int(input('Enter no. of servers: '))
processes = int(input('Enter no. of processess: '))

def balance_load(servers, processes):
    if servers < 0:
        print("\nCannot remove more servers !!!\n")
        return
    elif processes < 0:
        print("No more processess !!!")
        return

    print(f"\nThere are now {servers} Servers and {processes} process.\n")

while True:
    balance_load(servers, processes)

    choice = int(input("1.Add Server\n2.Remove Server\n3.Add Process\n4.Remove Process\n5.Exit\nEnter your choice: "))

    if choice == 1:
        if servers < 0:
            servers = 1
        else:
            servers += 1
    elif choice == 2:
        servers -= 1
    elif choice == 3:
        if processes < 0:
            processes = 1
        else:
            processes += 1
    elif choice == 4:
        processes -= 1
    else:
        break

