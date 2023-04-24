m = int(input())
n = int(input())

lst = []
sum = 0
for i in range(m, n+1):
    cnt=0
    for k in range(1, i+1):
        if i%k==0:
            cnt+=1
    if cnt==2:
        lst.append(i)
        sum+=i
        
if sum==0:
    print(-1)
else:
    print(sum)
    print(lst[0])