n = int(input())
c = 1
count = 0
while c <= n:
    if c == n:
        count += 1
        print('верно')
        break
    else:
        c = c * 2
if count == 0:
    print('неверно')
