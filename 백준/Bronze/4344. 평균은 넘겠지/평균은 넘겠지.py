c = int(input())
score = []
for i in range(0, c):
    new = list(map(int, input().split()))
    sum = 0
    great = 0
    for k in range(1,new[0]+1):
        sum+=new[k]
    for k in new[1:]:
        if k>sum/new[0]:
            great+=1
    score.append(round(great/new[0]*100, 3))

for i in range(c):
    print("%.3f" %score[i], "%", sep='')