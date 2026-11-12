r = []
c = 0
while True:
    n = float(input())
    if n == 0:
        break
    r.append(n)
    if len(r) == 2:
        if r[0] > r[1]:
            c += 1
        r.pop(0)
print(c)

