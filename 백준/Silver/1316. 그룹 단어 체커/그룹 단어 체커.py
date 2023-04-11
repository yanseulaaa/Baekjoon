n = int(input())
words = []
group = 0
for i in range(n): words.append(input())

for word in words:
    alph = []
    for ch in word:
        if ch not in alph:
            alph.append(ch)
        else:
            if ch != alph[-1]:
                break
    else:
        group +=1

print(group)