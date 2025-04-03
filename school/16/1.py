def f(n):
    if n ** 0.5 % 2 == 0 or n ** 0.5 % 2 == 1:
        return n ** 0.5
    else:
        return f(n + 1) + 1
print(f(4850) + f(5000))