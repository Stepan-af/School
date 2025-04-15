s = "5" * 20
cnt = 0
while "5555" in s:
    s = s.replace("5555", "45", 1)
    cnt += 1
print(cnt)