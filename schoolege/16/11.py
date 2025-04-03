import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n <= 12:
        return 1
    if n > 12:
        return f(n - 1) + n - 2
print(f(2024) - f(2020))