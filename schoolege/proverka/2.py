a = []
for n in range(1234567891011121, 10000000000000000):
    s = str(n)[::-1]
    sm = 0
    for i in range(len(s)):
        if i % 2 == 0:
            sm = sm + int(s[i])
        else:
            uv = int(s[i]) * 2
            if uv > 9:
                b = uv % 10 + uv // 10
                sm += b
            else:
                sm += uv
    if sm % 10 == 0:
        print(n)
        break