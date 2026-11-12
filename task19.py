n = int(input())
s = 0
for i in range(0,n+1):
    for j in range(0,n+1):
        if i != j:
            s += (i + j) / 2
        else:
            s += i + j
print(int(s))