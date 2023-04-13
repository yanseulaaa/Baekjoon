n, m = map(int, input().split())

matrixA = []
matrixB = []

for i in range(n): matrixA.append(list(map(int, input().split())))
for i in range(n): matrixB.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        print(matrixA[i][j]+matrixB[i][j], end = ' ')
    print("")