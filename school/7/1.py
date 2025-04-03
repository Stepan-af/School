from math import *
k1 = 96 * 54
k2 = 64 * 36
ppi1 = 600 * 600
ppi2 = 300 * 300
v1 = 27 * 1024 * 1024 * 8
i1 = v1 / (k1 * ppi1)
i2 = i1 / 1.5
v2 = k2 * ppi2 * i2
print((v1 - v2) / 8 / 1024)
