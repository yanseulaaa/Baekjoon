n = int(input())
dot = 4
line = 2
for i in range(n):
    dot += 4**(i) + (2**i)*(line*2)
    line = line*2-1
print(dot)