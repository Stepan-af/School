a = []
for n in range(13):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = "10" + s
    else:
        s = "1" + s + "01"
    r = int(s, 2)
    a.append(r)
print(max(a))