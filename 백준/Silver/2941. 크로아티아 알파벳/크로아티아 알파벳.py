c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
count = len(word)

for i in range(len(word)-1):
    if word[i:i+2] in c:
        count-=1

for i in range(len(word)-2):
    if word[i:i+3] in c:
        count-=1

print(count)