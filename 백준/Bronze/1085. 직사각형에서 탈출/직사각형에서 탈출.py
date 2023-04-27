x, y, w, h = map(int, input().split())

min = 0

if x<y:
    min = x
else:
    min = y

if w-x<min:
    min = w-x
if h-y<min:
    min = h-y

print(min)