lists = []
for i in range(0,9):
    lists.append(int(input()))
max = lists[0]
idx = 1
for i, val in enumerate(lists):
    if val>max: 
        max = val
        idx = i+1

print(max, idx, sep = '\n')