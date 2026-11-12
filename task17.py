n = int(input())
while True:
    print('{:.3f}'.format(n ** 0.5))
    if n ** 0.5 < 2:
        break
    n = n ** 0.5