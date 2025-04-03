from itertools import *
def func(n, k, m, l):
    return (not n) or k and (not m) or (l == m)
s = set()
for a, b, c, d in product([0, 1], repeat=4):
    t = ((0, 1, 0, a, 0), (b, 0, 0, c, 0), (1, 0, d, 1, 0))
    if len(t) == len(set(t)):
        for p in permutations("nkml"):
            if all(func(**dict(zip(p, r))) == r[-1] for r in t):
                s.add(p)
print(*s)