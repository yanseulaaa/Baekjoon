n, m = map(int, input().split())

basket = [i+1 for i in range(0,n)]

for cnt in range(0,m):
    i, j = map(int, input().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp
    
for val in basket:
    print(val, end = ' ')