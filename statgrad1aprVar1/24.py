from re import findall
base = ''
s = open(base + '24.txt').readline().strip()
arr = findall(r'[1-9][0-9]{5}(?:\*[1-9][0-9]{5})+(?:-[1-9][0-9]{5})*', s)
arr1 = findall(r'[1-9][0-9]{5}(?:-[1-9][0-9]{5})+', s)
print(max(len(x) for x in arr + arr1))