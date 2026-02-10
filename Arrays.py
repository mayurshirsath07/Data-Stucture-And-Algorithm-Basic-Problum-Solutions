#Basic Array represantation

import array as arr
a=arr.array('i',[1,2,3,4])
print(a)

# Adding a Element of an Array
# there are two type to Add An Element 
# 1) insert('index', 'numbers')
# 2) Append(only one number)

a.insert(4,5)
print(a)
a.append(6)
print(a)

# accessing array elements of an Array with the index nos

print("access the position of ",a[0])
print("access the position of ",a[3])

# revoming element from array
# there have 2 mathods 
# 1) remove() ----> remove the 1 st occurance of array
# 2) pop() ----> remove the items at index position

a.append(1)
print(a.remove(1),"the removed array", a)
print(a.pop(5),"the pop array", a)

a.append(7)
print(a)

# Slicing of an array 

b= arr.array('i',a)
print("the b array",b)
#element within a range
res=a[3:7]
print(res)
#element from specific index till the end 
res=a[4:]
print(res)
#print complete list 
res=a[:]
print(res)