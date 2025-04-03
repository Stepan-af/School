from itertools import *
def func(x, y, w):
    return (not(x) or y) and (w or not(w))
k = set()
for a, b, c in product([0, 1], repeat=3):
    t = [(1, 1, 0), (a, 1, b), (1, 0, 1), (1, c, 1)]
    if len(t) == len(set(t)):
        for p in permutations("xyw"):
            if all(func(**dict(zip(p, r))) == r[-1] for r in t):
                k.add(p)
print(*k)