from itertools import *
def func(u, w, x, y):
    return (not((not(y) or w) == x) and u)
k = set()
for a, b, c in product([0, 1], repeat=3):
    t = ((0, 1, 0, a, 0), (0, 1, 1, 1, 0), (1, 0, 1, b, 1), (1, c, 1, 1, 1))
    if len(t) == len(set(t)):
        for p in permutations("uwxy"):
            if [func(**dict(zip(p, r))) for r in t] == [0, 0, 1, 1]:
                k.add(p)
print(*k)