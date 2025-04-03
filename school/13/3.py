mask = [int('1'*i+'0'*(8-i),2) for i in range(9)]
print(*[m for m in mask if 93 & m == 80])