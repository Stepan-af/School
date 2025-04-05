import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n <= 5:
        return 1000
    if n > 5:
        return n + 3 + f(n - 2)
print(3 * f(53080) - (f(53078) + f(53076) + f(53074)))