n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

sum = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum.append(cards[i]+cards[j]+cards[k])

sum.sort(reverse=True)
for i in sum:
    if i<=m:
        print(i)
        break