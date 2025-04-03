# f = [1, 1] + [0] * 2041
# for n in range(2, 2043): 
#     f[n] = [f[n - 1], f[n - 1] + f[n - 2] + f[1]][n % 100 == 0] + 1 
# print(f[2042])


from functools import *
import sys
sys.setrecursionlimit(3000)
lru_cache(None)
def f(n):
    if n < 1:
        return 1
    elif n > 1 and n % 100 == 0:
        return 1 + f(n - 1) + f(n - 2) + f(1)
    elif n > 1:
        return 1 + f(n - 1)
    else:
        return 1
print(f(2042))
