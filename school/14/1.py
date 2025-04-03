def f(n):
    s = ''
    while n:
        s = str(n % 5) + s
        n = n // 5
    return s
a = []
for x in range(1, 2031):
    b = f(5 ** 100 - x)
    a.append([b.count("0"), x])
a = sorted(a)
print(a)