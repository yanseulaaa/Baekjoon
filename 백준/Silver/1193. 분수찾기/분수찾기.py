x = int(input())
n=1
m=1
for i in range(0, x):
    if i*(i+1)/2 < x and x <= (i+2)*(i+1)/2:
        n = i
        m = x - i*(i+1)/2
        break

if (n+1)%2 != 0:
    print("%d/%d" %(n+2-m, m))
else:
    print("%d/%d" %(m, n+2-m))