a, b =input().split()
a = a[::-1]
b = b[::-1]

result = ''
c = 0

while len(a)!=len(b):
    if len(a)>len(b):
        b += '0'
    else:
        a += '0'

for i in range(len(a)):
    sum = int(a[i])+int(b[i])+c
    if sum>=10:
        c = 1
        result += str(sum%10)
    else:
        c = 0
        result += str(sum)
if c==1: result+='1'

print(result[::-1])