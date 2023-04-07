n = int(input())
arr = list(map(int, input().split()))
max = arr[0]
min = arr[0]
for i in arr:
    if i<min: min = i
    if i>max: max = i

print(min, max)