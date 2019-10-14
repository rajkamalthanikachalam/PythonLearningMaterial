# List is collection of different data(can be integer, char,..) but it should written within square brackets

# Assigning list values
list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = ["Abc", "Def", "Ghi"]
print(list2)

# shallow or creating a copy
print(list1[:])
print(list2[:])

# length of list
print(len(list1))
print(len(list2))

# SubString
print(list1[0])
print(list1[0:2])
print(list1[3:5])

# print value based on indexing
# Slicing : It maintain negative indexing
print("Positive indexing %s" % list1[0])
print("Positive indexing %s" % list2[2])
print("Negative indexing %s" % list1[-1])  # Slicing
print("Negative indexing %s" % list2[-2])  # Slicing

# Assign value in the list
print("Before assigning the list value %s" % list2)
list1[2] = 100  # assigning value to the specific index
print("After assigning the list value %s" % list2)

# concatenation Adding value to the list
print(list1 + [7, 8, 9])
# print(list1 + ["x", "y", "z"])   # Can concatenate string also

print("Before Appending the list %s" % list2)
list2.append("Jkl")  # appending value to the list and it takes only one argument
print("After Appending the list %s" % list2)
list2.append("JKL")
print("After Appending the list %s" % list2)
list2.append(3**3)  # ** is used for cube of (i.e 3*3*3)
print("After Appending the list %s" % list2)

print("Before Replacing the list %s" % list2)
list2[2:4] = ["Replaced with text 1", "Replaced with text 2", "Replaced with text 3"]  # you can add list this way too
print("After Replacing the list %s" % list2)

# delete the list value
list2[2:5] = []  # delete the value for specific array
print("Deleting specific array in a list %s" % list2)

print("Before deletion %s" % list2)
list2[:] = []
print("After deletion %s" % list2)

# Nested List
a = [1, 2, 3]
b = ["Raj", "Kamal", "Thanikachalam"]
c = [a, b]
print("Nested list %s" % c)

print("Print value of First index %s" % c[0])
print("Print value of Second index %s" % c[1])
# print value from specific index, not a 2 dimension array
print("Print value of specific value in first index %s" % c[0][2])
print("Print value of  specific value in second index %s" % c[1][1])
