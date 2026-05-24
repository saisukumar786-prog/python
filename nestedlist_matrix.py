list1 = [[1,2,1],[2,1,3],[0,1,4]]
list2 = [[1,1,1],[1,1,1],[1,1,1]]

addition = []
for i in range(len(list1)):
    row = []
    for j in range(len(list1[i])):
        row.append(list1[i][j] + list2[i][j])
    addition.append(row)

multiplication = []
for i in range(len(list1)):
    row = []
    for j in range(len(list2[0])):
        total = 0
        for k in range(len(list2)):
            total += list1[i][k] * list2[k][j]
        row.append(total)
    multiplication.append(row)

transpose = []
for j in range(len(list1)):
    row = []
    for i in range(len(list1[0])):
        row.append(list1[i][j])
    transpose.append(row)

print("Addition:")
print(addition)
print("Multiplication:")
print(multiplication)
print("Transpose:")
print(transpose)
