from itertools import *
def func(c, a, t, s):
    return (c or not(a)) or not(not(t) or s) or c
k = set()
for l, m, n, d, f, g in product([0, 1], repeat = 6):
    table = ((l, m, n, 1, 0), (d, 0, 1, 1, 0), (1, f, 1, g, 0))
    if len(table) == len(set(table)):
        for p in permutations("cats"):
            if [func(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                k.add(p)
print(*k)