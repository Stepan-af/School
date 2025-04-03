from functools import *
@lru_cache(None)

def f(n):
    if n == 1:
        return 2
    if n > 1 and f(n - 1) < 7555444:
        return f(n - 1) + 6
    else:
        return f(n - 1) - 7555444
mx = -1
for i in range(1,7555480):
    mx = max(mx, f(i))
print(mx)