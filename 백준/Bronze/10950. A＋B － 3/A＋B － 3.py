lists = []
case = int(input())
for i in range(0, case):
    a, b = map(int, input().split())
    lists.append(a+b)
for i in lists:
    print(i)
