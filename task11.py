r = []
while True:
    n = int(input())
    if n == -1:
        break
    r.append(n)
r.sort()
print(r[-1])