submit = []
for i in range(0,28): submit.append(int(input()))

no = []
for n in range(1, 31):
    if n not in submit:
        no.append(n)
no.sort()

for i in no:
    print(i)