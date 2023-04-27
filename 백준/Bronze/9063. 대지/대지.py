n = int(input())

dots = []
for i in range(n):
    dots.append(list(map(int, input().split())))

x1, x2, y1, y2 = dots[0][0], dots[0][0], dots[0][1], dots[0][1]

for dot in dots:
    if dot[0]<x1:
        x1 = dot[0]
    if dot[0]>x2:
        x2 = dot[0]
    if dot[1]<y1:
        y1 = dot[1]
    if dot[1]>y2:
        y2 = dot[1]

print((x2-x1)*(y2-y1))