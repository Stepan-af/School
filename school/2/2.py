from itertools import *
def u(a, b, c):
    return not(a) or not(b) and c
k = set()
t = [(0, 1, 0, 0), (0, 1, 1, 0), (1, 1, 1, 0)]
for p in permutations("abc"):
    if all(u(**dict(zip(p, r))) == r[-1] for r in t):
        k.add(p)
print(*k)