num = 0

st = input()

for ch in st:
    if ch == 'A' or ch == 'B' or ch == 'C':
        num += 3
    elif ch == 'D' or ch == 'E' or ch == 'F':
        num += 4
    elif ch == 'G' or ch == 'H' or ch == 'I':
        num += 5
    elif ch == 'J' or ch == 'K' or ch == 'L':
        num += 6
    elif ch == 'M' or ch == 'N' or ch == 'O':
        num += 7
    elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
        num += 8
    elif ch == 'T' or ch == 'U' or ch == 'V':
        num += 9
    elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
        num += 10

print(num)