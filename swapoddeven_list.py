list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, len(list1) - 1, 2):
    list1[i], list1[i + 1] = list1[i + 1], list1[i]

print(list1)
