def div(n):
    d = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d
def prime(i):return i >= 2 and all(i % j !=0 for j in range(2, int(i**0.5)+1))
k = 0
for i in range(1_825_001, 2_000_000):
    de = [x for x in div(i)]
    pr = [x for x in de if prime(x)]
    try:
        if max(pr) <= 25_000 and max(pr) % 10 == 3:
            print(i)
            k += 1
            if k == 5:
                break
    except:
        ...