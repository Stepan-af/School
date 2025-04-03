from itertools import *
def func(a, b, c, d):
    return (not(a) or b) and (not(b) or c) and (not(c) or d)
k = set()
for m, l in product([0, 1], repeat=2):
    t = ((0, m, 1, 0, 1), (0, l, 1, 0, 1), (0, 1, 1, 1, 1))
    if len(t) == len(set(t)):
        for p in permutations("abcd"):
            if [func(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                k.add(p)
print(*k)