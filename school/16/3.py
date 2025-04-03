cnt = 0
def f(n):
    if n < 10:
        return n
    if n >= 10 and n < 1000:
        return f(n // 10) + f(n % 10)
    if n >= 1000:
        return f(n // 1000) - f(n % 1000) 
for i in range(10 ** 6):
    if f(i) == 0:
        cnt += 1
print(cnt)