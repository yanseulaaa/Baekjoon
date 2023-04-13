matrix = []
for i in range(9): matrix.append(list(map(int, input().split())))

max = matrix[0][0]
m = 1
n = 1

for i in range(9):
    for j in range(9):
        if matrix[i][j]>max:
            m, n = i+1, j+1
            max = matrix[i][j]

print(max)
print(m, n, sep = ' ')