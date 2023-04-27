dots = []

for i in range(3):
    dots.append(list(map(int, input().split())))

x = 0
y = 0

if dots[0][0] == dots[1][0]:
    x = dots[2][0]
elif dots[0][0] == dots[2][0]:
    x = dots[1][0]
else:
    x = dots[0][0]

if dots[0][1] == dots[1][1]:
    y = dots[2][1]
elif dots[0][1] == dots[2][1]:
    y = dots[1][1]
else:
    y = dots[0][1]

print(x, y)