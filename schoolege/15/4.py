def d(n, m):
    if n % m == 0:
        return True
    else:
        return False


for a in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if not(d(x, 30) and not(d(x, 45))) or not(d(x, a)):
            k += 1
    if k == 1000:
        print(a)
        break
    