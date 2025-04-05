def f(x):
    p = 215 <= x <= 264
    q = 221 <= x <= 294
    a = a1 <= x <= a2
    return (not(p <= (((not a) and q) <= (not p))))
d = [y for x in (215, 221, 264, 294) for y in (x, x - 0.5, x + 0.5)]
res = []
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x)==0 for x in d):
            res.append((a2 - a1))
print(min(res))