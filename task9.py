n,k,r = map(int,input().split())
c = 1
while n < r:
    if n * (1 + k / 100) >= r:
        c += 1
        break
    else:
        c += 1
        n = n * (1 + k / 100)
print(c)