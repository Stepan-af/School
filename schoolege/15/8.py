def f(x):
    b = 74 <= x <= 194
    c = 152 <= x <= 223
    a = a1 <= x <= a2
    return not(not(a) and b) or (not(b) or not(c))
d = [y for x in (74, 194, 152, 223) for y in (x, x - 0.5, x + 0.5)]
res = []
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) for x in d):
            res.append(a2 - a1)
print(min(res))