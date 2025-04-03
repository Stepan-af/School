from ipaddress import *
net = ip_network("192.168.32.160/255.255.255.240")
bin_adress = [f"{address:b}" for address in net]
cnt = 0
for address in bin_adress:
    if address.count("1") % 2 == 0:
        cnt += 1
print(cnt)