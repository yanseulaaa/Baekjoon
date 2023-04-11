word = input()
word = word.upper()
alph = dict()

for i in word:
    if i in alph.keys():
        alph[i] += 1
    else:
        alph[i] = 1

most = ''
val = 0

for a, c in alph.items():
    if c>val:
        val = c
        most = a
    elif c == val:
        most = '?'

print(most)