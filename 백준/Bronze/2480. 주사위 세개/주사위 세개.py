a, b, c = map(int, input().split())

if a==b and b==c:
    p = 10000 + a*1000
elif a==b or b==c :
    p = 1000 + b*100
elif a==c:
    p = 1000 + c*100
else:
    if a>b and a>c:
        p = a*100
    elif b>a and b>c:
        p = b*100
    else:
        p = c*100

print(p)