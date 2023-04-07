n, m = map(int, input().split())
b = [i+1 for i in range(0,n)]
for i in range(0,m):
    i, j = map(int, input().split())
    while(i<j):
        temp = b[i-1]
        b[i-1] = b[j-1]
        b[j-1] = temp
        i+=1
        j-=1
for val in b:
    print(val, end = ' ')