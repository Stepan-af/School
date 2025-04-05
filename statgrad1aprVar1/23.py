def f(x, y):
    if x == y: return 1
    if x < y or x == 9: return 0
    else:
        return f(x - 1, y) + f(x // 2, y)
print(f(65, 31) * f(31, 14) * f(14, 4))