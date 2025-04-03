def f(x, y, h):
    if h == 3 and x * y >= 123:
        return 1
    elif h == 3 and x * y < 123:
        return 0
    elif h < 3 and x * y >= 123:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 2, y, h + 1) or f(x, y + 2, h + 1) or f(2 * x, y, h + 1) or f(x, 2 * y, h + 1)
        else:
            return f(x + 2, y, h + 1) or f(x, y + 2, h + 1) or f(2 * x, y, h + 1) or f(x, 2 * y, h + 1)
for i in range(41, 1, -1):
    if f(3, i, 1) == 1:
        print(i)
        break