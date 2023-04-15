t = int(input())
c = []
for i in range(t): c.append(int(input()))

for i in c:
    q=i//25
    i=i%25

    d=i//10
    i=i%10

    n=i//5
    i=i%5

    p=i//1

    print(q, d, n, p)
