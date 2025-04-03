from itertools import *
def func(a, b, c):
    return b == (not(a or c) or b)


def func1(a, b, c):
    return b == (a or (not(c) or b))
k = set()
t = ((0, 1, 0), (0, 1, 1), (1, 0, 1))
if len(t) == len(set(t)):
    for p in permutations("abc"):
        if ([func(**dict(zip(p, r))) for r in t] == [1, 1, 1]) and ([func1(**dict(zip(p, r))) for r in t] == [1, 1, 1]):
            k.add(p)
print(*k)