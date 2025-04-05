from ipaddress import *
mx = 0
for m in range(33):
    net = ip_network(f"145.46.8.250/{m}", strict=False)
    if "145.46.0.0" in str(net):
        for ip in net:
            if ip != net.broadcast_address:
                mx = max(mx, bin(int(ip)).count("1"))
print(mx)