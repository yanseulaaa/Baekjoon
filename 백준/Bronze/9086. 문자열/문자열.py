t = int(input())
case = []
for i in range(0,t): case.append(input())

for i in range(0,t):
    print(case[i][0], case[i][-1], sep='')