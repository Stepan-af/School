for a in range(1000):
    k = 0
    for x in range(1000):
        if not(x & 52 == 4) or (not(x & 26 == 2) or (x & a == 6)):
            k += 1
    if k == 1000:
        print(a)
        