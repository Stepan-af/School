a = []
for n in range(26, 1000):
    s = bin(n)[2:]
    s = str(s)
    if n % 2 != 0:
        s = s[:-2] + '10'
    else:
        s += '1'
        s = '10' + s[2:]
    r = int(s, 2)
    a.append(r)
print(min(a))
