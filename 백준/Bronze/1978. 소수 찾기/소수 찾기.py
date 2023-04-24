n = int(input())

lst = list(map(int, input().split()))

result = 0
for k in lst:
    cnt = 0
    for i in range(1,k+1):
        if k%i==0:
            cnt+=1
    if cnt==2:
        result+=1

print(result)