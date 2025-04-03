def f(x, a): return not((x | 50 > 70) and (x | 17 <= 108)) or ((x | 108 > 17) and (x | a < 108))
for a in range(1000):
    if all(f(x, a) for x in range(1000)):
        print(a)