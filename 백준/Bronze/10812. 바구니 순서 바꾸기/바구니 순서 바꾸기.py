n, m = map(int, input().split())
b = [i for i in range(1, n+1)]

for a in range(0, m): 
    i, j, k = map(int, input().split())
    new = []
    for c in range(k, j+1):
        new.append(b[c-1])
    for c in range(i, k):
        new.append(b[c-1])
    for c in range(0, j-i+1):
        b[i-1+c] = new[c]

for i in b: print(i, end = ' ')