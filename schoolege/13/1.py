from ipaddress import *
mx = -10**10
for mask in range(32+1):
    net = ip_network(f'117.73.208.27/{mask}', 0)
    if str(net) == f'117.73.192.0/{mask}':
        mx = max(mx, mask)
print(mx)