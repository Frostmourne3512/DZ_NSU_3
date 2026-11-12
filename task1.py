r = []
c = 0
for i in range(100,1000):
    if i % 17 == 0:
        c += 1
        r.append(str(i))
print(' '.join(r),c,sep='\n')
