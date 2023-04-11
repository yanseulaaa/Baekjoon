grades = {'A+': 4.5, 'A0': 4.0, 'B+':3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 
          'D+': 1.5, 'D0': 1.0, 'F': 0}
lists = []
semester = dict()
for i in range(0,20): lists.append(input())

for val in lists:
    sub, credit, grade = map(str, val.split())
    semester[sub] = [float(credit), grade]

cnt = 0
sum = 0
for i in semester.keys():
    if semester[i][1] != 'P':
        cnt += semester[i][0]
        sum += semester[i][0] * grades[semester[i][1]]

print(sum/cnt)
