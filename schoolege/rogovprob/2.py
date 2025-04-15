from itertools import *
def func(x, y, z, w):
    return (z != y) and (not(x) or y) and w
k = set()
for a, b, c, d, e, f in product([0, 1], repeat=6):
    t = ((1, a, b, 0), (0, 0, c, 1), (d, e, f, 1))
    if len(t) == len(set(t)):
        for p in permutations("xywz"):
            if [func(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                k.add(p)
print(k)