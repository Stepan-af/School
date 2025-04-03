from itertools import *
def u(x, y, z):
    return x and y or not(y) and not(z)
t = [(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1)]
k = set()
for p in permutations("xyz"):
    if all(u(**dict(zip(p, r))) == r[-1] for r in t):
        k.add(p)
print(*k)