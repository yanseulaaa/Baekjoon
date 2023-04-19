n = int(input())

count = 1
r=n-1

for i in range(1, n):
    r = r-6*i
    count+=1
    if r<=0:
        break
    
print(count)