def f(x,h):
    if h == 4 and x >= 82:
        return 1
    elif h == 4 and x < 82:
        return 0
    elif h < 4 and x >= 82:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 2, h + 1) or f(x + 4, h + 1) or f(3 * x, h + 1)
        else:
            return f(x + 2, h + 1) and f(x + 4, h + 1) and f(3 * x, h + 1)
for i in range(1, 82):
    if f(i, 1) == 1:
        print(i)