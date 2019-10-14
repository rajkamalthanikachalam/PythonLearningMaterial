# no need to define the data type for a variables
# Indentation is important, wrong indent may lead to error
# It has inbuilt naming conventions/rules or standards (A-Z, a-z, 0-9)
# Single value can be assigned to multiple variables
# we can use comma separator to print multiple value in single print statement
# existing functions like sub string, concatenation, printing the multiple value at once print statement
# print the output multiple times as required
# indent matters, tabbing of this print will change the format of output

a = 10
a = a + 20
print(a)

#  Indentations
if a > 10:
    print("A is greater")
else:
    print("A is lesser")

# not declaring data type for variables and same variable is used to define the different data type
i = 10
print(i)

i = 10.5
print(i)

i = "Test String"
print(i)

# to Identify/prove the same ID is allocated to different variable, if both shares the same value
x = 100
y = x

print(x)
print(y)
print(id(x))        # id() is used to identify/prove the same ID is allocated to different variable
print(id(y))        # id() is used to identify/prove the same ID is allocated to different variable

# inbuilt feature, Naming conventions, standards/rules to define the variables
# minbal = 100  # will throw warning
min_bal = 100
print(min_bal)

NameOfTheBook = "Rise of the Kingdom"   # like Java, can be used
print(NameOfTheBook)
Name_of_the_book = "Rise of the Kingdom"  # suggested approach, for more readability
print(Name_of_the_book)

# Single value can be assigned to multiple variables
i = j = k = 10
print(i)
print(j)
print(k)

# Multiple values can be assigned to multiple variables
a, b, c = 10, 50.25, "Test"
print(a)
print(b)
print(c)

# we can use comma separator to print multiple value in single print statement
print(i, j, k)
print(a, b, c)

# existing functions like sib string, concatenation
s = "Hey this is my first python program"

print(s)
print(s[0])  # to print first character
print(s[2:10])  # to print character from 3 to 9
print(s[2:])  # to print character from 2 to end
print(s*2)  # to print the s value twice
print(s*5)  # to print the s value 5 times
