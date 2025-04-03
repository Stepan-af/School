def f(x):
    b = 101 <= x <= 143
    c = 144 <= x <= 199
    a = a1 <= x <= a2
    return not(a) or (b or c)
d = [y for x in (101, 143, 144, 199) for y in (x, x - 0.5, x + 0.5)]
res = []
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) for x in d):
            res.append(a2 - a1)
print(max(res))