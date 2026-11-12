n = int(input())
r = []
for i in range(1,(n**0.5)+1):
    for j in range(1,(n**0.5)+1):
        if i ** 2 + j ** 2 == n:
            a = str(i+j)
            if a not in r:
                r.append(a)
print(r)