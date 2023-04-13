matrix = []
for i in range(5): matrix.append(list(input()))

for j in range(15):
    for i in range(5):
        if j<len(matrix[i]):
            print(matrix[i][j], sep = '', end='')