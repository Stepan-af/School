def f(x, h):
    if h == 3 and x >= 61:
        return 1
    elif h == 3 and x < 61:
        return 0
    elif h < 3 and x >= 61:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 3, h + 1) or f(x + 10, h + 1) or f(2 * x, h + 1)
        else:
            return f(x + 3, h + 1) or f(x + 10, h + 1) or f(2 * x, h + 1)
for i in range(1, 61):
    if f(i, 1) == 1:
        print(i)
        break