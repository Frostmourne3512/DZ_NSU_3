n = int(input())
r = []
i = 1
while True:
    if i ** 3 <= n:
        r.append(str(i ** 3))
        i += 1
    else:
        break
print(' '.join(r))

