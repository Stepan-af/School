from itertools import *
def func(w, x, y, z):
    return (not(not(w) or y) or x) or not(z)
k = set()
for a, b, c, d, e, f, g in product([0, 1], repeat = 7):
    t = ((a, b, 1, c, 0), (d, 0, e, f, 0), (g, 1, 0, 0, 0))
    if len(t) == len(set(t)):
        for p in permutations("wxyz"):
            if [func(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                k.add(p)
print(*k)