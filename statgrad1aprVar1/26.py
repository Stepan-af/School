f = open("24.txt")
n = int(f.readline())
time = {i: 0 for i in range(1441)}
for i in f:
    i, o = map(int, i.split())
    for x in range(i, o + 1):
        time[x] += 1
chg = []
mxtime = 0
tmp = 1
for x in range(1440):
    if time[x] == time[x + 1]:
        tmp += 1
    else:
        mxtime = max(mxtime, tmp)
        tmp = 1
        chg.append(x + 1)
print(chg[-2], mxtime)