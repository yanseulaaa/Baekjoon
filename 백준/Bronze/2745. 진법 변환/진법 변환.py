n, b = input().split()
b = int(b)
digit=len(n)
result = 0
while digit>0:
    for i in n:
        v = 0
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
            v = 10+ord(i)-ord('A')
        else:
            v = int(i)

        result += v*b**(digit-1)
        digit-=1

print(result)