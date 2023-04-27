a,b,c = sorted(map(int, input().split()))

while 1:
    if a+b>c:
        print(a+b+c)
        break
    c-=1