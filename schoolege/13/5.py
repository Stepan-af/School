from ipaddress import *
net = ip_network("136.36.240.16/255.255.255.248")
bin_address = [f"{address:b}" for address in net]
cnt = 0
for address in bin_address:
    if "101" not in address:
        cnt += 1
print(cnt)