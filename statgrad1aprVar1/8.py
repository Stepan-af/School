from itertools import *
alp = "БЛРСУЬЭ"
k = 0
a = []
for i, x in enumerate(product(alp, repeat=5), 1):
    s = "".join(x)
    if i % 2 == 0 and s.count("С") >= 2 and s.count("Л") == 1 and  "ЭЭ" not in s:
        print(i)