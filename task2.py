a = input()
s = ''
c = 0
for i in range(len(a)):
    c += 1
    if c % 3 == 0:
        s += a[i]
print(s)
