# f = [1, 1] + [0] * 2041
# for n in range(2, 2043): 
#     f[n] = [f[n - 1], f[n - 1] + f[n - 2] + f[1]][n % 100 == 0] + 1 
# print(f[2042])


from functools import *
import sys
sys.setrecursionlimit(3000)
lru_cache(None)
def f(n):
    if n < 1:
        return 1
    elif n > 1 and n % 100 == 0:
        return 1 + f(n - 1) + f(n - 2) + f(1)
    elif n > 1:
        return 1 + f(n - 1)
    else:
        return 1
print(f(2042))

def count_calls(n):
    if n < 1:
        return 1  # Базовый случай
    
    # Инициализация списка dp
    dp = [0] * (n + 1)
    dp[0] = 1  # F(0) требует 1 вызов
    
    for k in range(1, n + 1):
        if k % 100 == 0 and k > 1:
            # F(k) = F(k-1) * F(k-2) + F(1)
            dp[k] = 1 + dp[k - 1] + dp[k - 2] + dp[1]
        elif k > 1:
            # F(k) = k * F(k-1)
            dp[k] = 1 + dp[k - 1]
        else:
            # F(1) = 1 * F(0) = 1 * 1 = 1 → 1 вызов (F(1)) + 1 вызов (F(0))
            dp[k] = 1  # F(1) требует 2 вызова (F(1) и F(0))
    
    return dp[n]

# Вычисляем количество вызовов для F(2042)
result = count_calls(2042)
print(result)