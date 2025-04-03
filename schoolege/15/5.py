def d(n, m):
    if n % m == 0:
        return True
    else:
        return False


for a in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if not(not(d(x, a)) and d(x, 24)) or (not(d(x, 16)) or not(d(x, 24))):
            k += 1
    if k == 1000:
        print(a)