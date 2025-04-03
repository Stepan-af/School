def f(a, x, y):
    return (x * y > a) or (x > y) or (8 > x)
for a in range(100):
    if all(f(a, x, y) for x in range(100) for y in range(100)):
        print(a)