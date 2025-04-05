s = "2" + "3" * 110
while "2" in s:
    if "23" in s:
        s = s.replace("23", "332", 1)
    else:
        s = s.replace("2", "33", 1)
# print(sum(map(int, s)))
print(s.count("2") * 2 + s.count("3") * 3)