n, m = map(int, input().split())

basket = [0 for i in range(0,n)]

for cnt in range(0,m):
    i, j, k = map(int, input().split())
    for put in range(i-1, j):
        basket[put] = k
    
for val in basket:
    print(val, end = ' ')