def f(a, x, y):
    return (not(x < a) or (x * x <= 169)) and (not(y * y < 16) or (y <= a))
for a in range(100):
    if all(f(a, x, y) for x in range(100) for y in range(100)):
        print(a)