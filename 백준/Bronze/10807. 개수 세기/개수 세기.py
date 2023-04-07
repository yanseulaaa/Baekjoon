n = int(input())
lists = list(map(int, input().split()))
v = int(input())

count = 0
for i in lists:
    if i == v:
        count+=1

print(count)