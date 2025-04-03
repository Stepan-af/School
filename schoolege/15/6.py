for a in range(1000):
    k = 0
    for x in range(1000):
        if (x & 91 == 0) or (not(x & 77 == 0) or (x & a != 0)):
            k += 1
    if k == 1000:
        print(a)
        break