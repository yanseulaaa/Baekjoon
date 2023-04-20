case = []
a=1
b=1
while(a!=0 and b!=0):
    a, b = map(int, input().split())
    case.append([a, b])

case = case[:-1]

for i in case:
    if i[1]%i[0] == 0:
        print("factor")
    elif i[0]%i[1] == 0:
        print("multiple")
    else:
        print("neither")  