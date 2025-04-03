def max_div(n):
    divs = {0}
    for x in range(2, round(n ** 0.5) + 1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return max(divs)
print(max_div(1750006))
# n = 1750000
# i = 0
# while i < 5:
#     n += 1
#     md = max_div(n)
#     if md <= 15000 and md % 10 == 7:
#         print(n)
#         i += 1