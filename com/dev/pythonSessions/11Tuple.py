# Collection : Tuple, list, set, data set, dictionary
# Tuple : collection of elements od any python data type
# Tuple Vs List
# Tuple store value in () brackets
# List store value in [] brackets
# Tuple is immutable(Can't change value of tuple elements)
# List is mutable(can change the value)

tuple_num = (10, 20, 30, 40, 50)
tuple_alpha = ("Java", "Python", "C", "Ruby", "ASP.Net")

print("Tuple : %s" % str(tuple_num))
print("Tuple : %s" % str(tuple_alpha))
print("Tuple : Indexing : %d" % tuple_num[2])     # print specific index value
print("Tuple : Indexing : %s" % tuple_alpha[1])   # print specific index value
print("Tuple : Reverse Slicing : %s" % tuple_num[-1])    # slicing : reverse indexing
print("Tuple : Reverse Slicing : %s" % tuple_alpha[-4])  # slicing : reverse indexing
# tuple_num[2] = 1000       This line will throw error : "'tuple' object does not support item assignment"
# print("Value at 2 Index in List : %s " % tuple_num[2])    Tuple is immutable

#   Not Working, need to check
# print(tuple_num)
# del tuple_num
# print(tuple_num)
tuple_concatenation = str(tuple_num) + str(tuple_alpha)
print(tuple_concatenation)
tuple_print_multiple = (tuple_num*2)
print(tuple_print_multiple)
tuple_range = tuple_alpha[1:3]
print("Print tuple range : %s" % str(tuple_range))
tuple_in = ("Java" in tuple_alpha)      # in will return either true or false
print("Check it's in : %s " % tuple_in)

tuple_not_in = ("java" not in tuple_alpha)      # in will return either true or false
print("Check it's not in : %s " % tuple_not_in)

tuple_length = len(tuple_alpha)
print("Length of tuple : %s " % tuple_length)

tuple_max = max(tuple_alpha)    # Pick on the basis of first letter of elements, Capital took the priority
print("Maximum of : %s " % tuple_max)

tuple_min = min(tuple_alpha)
print("Minimum of : %s " % tuple_min)

print("******************************List***********************************************")

list_num = [10, 20, 30, 40, 50]
list_alpha = ["Java", "Python", "C", "Ruby", "ASP.Net"]
print("List Value : %s " % list_num)
print("Value at 2 Index in List : %s " % list_num[2])
list_num[2] = 1000
print("Value at 2 Index in List : %s " % list_num[2])   # mutable,same is not possible in Tuple
print("List Value : %s " % list_num)
list_range = list_num[:]    # to print all
print("List Range : %s" % list_range)
nested_list = [list_num, list_alpha]
print("Nested List %s " % nested_list[0][2])
print("Nested List %s " % nested_list[1][2])
