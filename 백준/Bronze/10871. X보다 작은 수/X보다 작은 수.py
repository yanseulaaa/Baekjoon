n, x = map(int, input().split())
a = list(map(int, input().split()))
small = [i for i in a if i<x]

for i in small:
    print(i, end=" ")