from decimal import Decimal as D
import sys
sys.setrecursionlimit(10000)
def f(n):
    if n <= 1:
        return D(1)
    if n > 1 and n % 2 == 0:
        return f(n - 1) / 3
    if n > 2 and n % 2 != 0:
        return 6 * f(n - 1)
print(f(2049) // f(2046))