list = [ 1, 0, 3, 4, 0, 6, 0, 8, 0, 10 ]
print(list)
for i in range(len(list)):
    if list[i]==0:
        del list[i]
        list.append(0)


print(list)        