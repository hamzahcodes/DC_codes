n = int(input("Enter the no. of sites: "))

request_set = {}

for i in range(1, n + 1):
    lst = []
    for j in range(1, n + 1):
        if i != j:
            lst.append(j)
    request_set[i] = lst

print(request_set)
n = int(input("Enter no. of sites who want to enter CS: "))

request_sites = []

for i in range(n):
    tupl = [int(x) for x in input("Enter the timestamp and site no. : ").split()]
    request_sites.append(tuple(tupl))

print(request_sites)

request_sites = sorted(request_sites)

for i in request_sites:
    for j in request_set[i[1]]:
        print(f"Site {i[1]} sending request to site {j}")

request_site = []

for i in request_sites:
    request_site.append(i[1])

print(request_site)
for tupl in request_sites:

    cur_req_site = tupl[1]

    for i in request_set[cur_req_site]:
        if i not in request_site:
            print(f"Site {i} Sending reply to {cur_req_site}")

        else:
            for j in request_sites:
                if i == j[1]:
                    if j[0] > tupl[0]:
                        print(f"Site {i} Sending reply to {cur_req_site}")


print(f"since site {cur_req_site} has received reply from all sites. it enters CS")

if(len(request_site)>0):
    print("\nSite {} exits the CS\n".format(cur_req_site))

request_site.pop(0)