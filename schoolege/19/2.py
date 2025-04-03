def f(x, y, h):
    if h == 2 and x + y >= 50:
        return 1
    elif h == 2 and x + y < 50:
        return 0
    elif h < 2 and x + y >= 50:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 3, y, h + 1) or f(x, y + 3, h + 1) or f(3 * x, y, h + 1) or f(x, 3 * y, h + 1)
        else:
            return f(x + 3, y, h + 1) or f(x, y + 3, h + 1) or f(3 * x, y, h + 1) or f(x, 3 * y, h + 1)
for i in range(2, 46):
    if f(4, i, 1) == 1:
        print(i)
        break