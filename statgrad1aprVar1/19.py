from functools import *
def win(p):
    return sum(p) <= 150
def steps(p):
    a, b = p
    return (a - 2, b), (a, b - 2), (a // 3, b), (a, b // 3)


@lru_cache(maxsize=None)
def win1(p, h):
    if h > 5: return -1
    if any(win(p) for p in steps(p)): return 1
    if any(win2(p, h + 1) == 1 for p in steps(p)): return 2
def win2(p, h):
    if h > 5: return -1
    if any(win(p) for p in steps(p)): return 1
    if all(win1(p, h + 1) == 1 for p in steps(p)): return 2
    if any(win1(p, h + 1) == 2 for p in steps(p)): return 3
def win3(p, h):
    if h > 5: return -1
    if any(win(p) for p in steps(p)): return 1
    if all(win3(p, h + 1) == 1 for p in steps(p)): return 2
    if any(win3(p, h + 1) == 2 for p in steps(p)): return 3
    if all(win3(p, h + 1) in [1, 3] for p in steps(p)): return 4
for s in range(10000, 130, -1):
    if win3((17, s), 0) == 4:
        print(s)