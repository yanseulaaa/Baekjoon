t = int(input())
r = []
s = []
for i in range(0,t):
    t, st = map(str, input().split())
    r.append(int(t))
    s.append(st)
for i, st in enumerate(s):
    for ch in st:
        print(ch*r[i], end='')
    print("")