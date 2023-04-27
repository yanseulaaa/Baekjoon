angles = []
while 1:
    a, b, c = map(int, input().split())

    if a==0 and b==0 and c == 0:
        break
    angles.append([a,b,c])

for i in angles:
    if i[0] == i[1] and i[1] == i[2] and i[2]==i[0]:
        print("Equilateral")    
    elif i[0]+i[1]<=i[2] or i[1]+i[2]<=i[0] or i[2]+i[0]<=i[1]:
        print("Invalid")
    elif i[0] == i[1] or i[1] == i[2] or i[2]==i[0]:
        print("Isosceles")
    else:
        print("Scalene")