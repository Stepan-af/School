from itertools import *
def func(w, x, y, z):
    return (w and z or not(w)) and x or y
k = set()
for a, b, c, d, e, f in product([0, 1], repeat=6):
    table = (0, a, 0, b), (c, 1, d, 1), (1, 1, e, f)
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [func(**dict(zip(p, r))) for r in table] == [1, 0, 0]:
                k.add(p)
print(*k)