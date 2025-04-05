f = open("17 (1).txt")
a = [int(x) for x in f]
res = []
sq = len([t for t in a if 1000 <= abs(t) <= 9999 and abs(t) % 10 == 3]) ** 2
cnt = 0
sm = 0
for i in range(len(a) - 2):
    x, y, z = a[i], a[i - 1], a[i - 2]
    if max(x, y, z) + (x + y + z) - max(x, y, z) - min(x, y, z) > sq:
        res.append(x + y + z)
        cnt += 1
print(cnt, max(res))
