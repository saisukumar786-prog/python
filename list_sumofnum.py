list1 = [123,67,63,45]
print (list1)
for i in range(len(list1)):
    temp =list1[i]
    sum = 0
    while temp >0 :
        a = temp % 10
        sum+=a
        temp = temp //10
        list1[i] = sum

print (list1)        