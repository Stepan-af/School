def f(n):
    if n > 10:
        return f(n - 1) + 3 * f(n - 3) + 2
    elif n % 2 == 0:
        return -1
    else:
        return 1
print(f(20))