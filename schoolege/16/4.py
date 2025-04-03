import sys
sys.setrecursionlimit(3000)
def f(n):
    if n >= 3210:
        return 1
    if n < 3210:
        return f(n + 3) + 7


def g(n):
    if n < 10:
        return n
    if n >= 10:
        return g(n - 3) + 5
print(f(15) - g(3000))