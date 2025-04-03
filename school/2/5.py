from itertools import *
def func(x, y, w, z):
    return (not(x) or y) or not(not(w) or z)
t = [(1, 0, 0, 1), (0, 0, 0, 1), (1, 0, 1, 1)]
for p in permutations("xywz"):
    if [func(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
        print(*p)
        