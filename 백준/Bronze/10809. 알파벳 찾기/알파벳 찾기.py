alph = "abcdefghijklmnopqrstuvwxyz"
s = input()

for i in alph:
    n = -1
    for j in range(0, len(s)):
        if s[j] == i:
            n = j
            break
    print(n, end = ' ')  