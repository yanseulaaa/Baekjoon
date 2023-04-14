n, b = map(int, input().split())
digit = 1
result = ''
while n>0:
    if n%b>=10:
        result = chr(n%b-10+ord('A'))+result
    else:
        result = str(n%b) + result
    n = n//b

print(result)