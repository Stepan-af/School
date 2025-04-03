from itertools import *
def u(x, y, w, z):
    return not(x) or y or (not(z) and w)
k = set()
t = [(0, 1, 0, 0, 0), (0, 1, 1, 0, 0), (1, 1, 1, 0, 0)]
for p in permutations("xywz"):
    if all(u(**dict(zip(p, r))) == r[-1] for r in t):
        k.add(p)
print(*k)