n = int(input())

paper = []
for i in range(n): paper.append(list(map(int, input().split())))
s = []

for square in paper:
    for i in range(10):
        for j in range(10):
            s.append(str(square[0]+i)+' '+str(square[1]+j))
print(len(set(s)))