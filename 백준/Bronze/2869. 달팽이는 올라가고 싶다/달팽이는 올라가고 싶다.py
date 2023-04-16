import math
a, b, v = map(int, input().split())

day = 0
c = 0

day = (v-a)/(a-b)+1

print(math.ceil(day))