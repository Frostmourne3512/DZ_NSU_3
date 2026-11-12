from math import *
n = int(input())
c = 1
for i in range(100):
    if ceil(n / 2) == 1:
        print(c)
        break
    else:
        c += 1
        n = int(ceil(n / 2))