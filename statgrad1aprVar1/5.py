def tri(a):
    r = ''
    while a:
        r = str(a % 3) + r
        a //= 3
    return r
res = []
for n in range(1, 1000):
    s = tri(n)
    st = sum(map(int, s))
    if st % 3 == 0:
        s = '112' + s[2:]
    else:
        s += tri(st)
    if int(s, 3) <= 679 and int(s, 3) % 2 == 0:
        res.append(int(s, 3))
print(max(res))
