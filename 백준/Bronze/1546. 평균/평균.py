n = int(input())
max = 0
score = list(map(int, input().split()))
for i in range(0,n): 
    if score[i]>max: max = score[i]
sum = 0
for i in score:
    sum += i/max*100
print(sum/n)