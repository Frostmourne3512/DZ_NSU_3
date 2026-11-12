n = int(input())
for i in range(n-1,-1,-1):
    s = ' ' * i
    for j in range(1,n+1):
        a = '*' * j
        if len(s + a) == n:
            print(s+a)

