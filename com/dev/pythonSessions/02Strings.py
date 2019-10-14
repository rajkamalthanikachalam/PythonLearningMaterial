# String declarations
# types of calling, using the string operators

# String declaration
str1 = "Hello world in double quotes"  # is preferred
str2 = 'Hello world in single quotes'  # single quotes can also used
print(str1)
print(str2)

print(str1[0])     # to identify the character at first position
print(str1[27])    # to identify the character at last position
print(str1[0:15])  # to identify the character at specific range
# print(str1[28])   # this will throw "string out of range" error

# concatenations
print(str1+str2)
print(str1+" "+str2)

# Alignments
print("str1 \n str2")  # to print second statement in next line
print("str1 \t str2")  # to print second statement after a tab

# Check
print("double" in str1)  # to identify the particular value is present in a statement or not, returns true or false
print("doubles" in str1)

print("double" not in str1)  # to identify the particular value is present in a statement or not, returns true or false
print("doubles" not in str1)

# Print options
# multiple times
print(str1*3)

# in paragraph,we can print between single or double  three quotes
print(""""Hi, there is a option in python,
 to print the lines 
 in different paragraph using the three double or single quotes""")

# to pass values during print - %s for string, %d for numeric with following formats
print("My Name is %s and I like to travel atleast %d country during my lifetime" % ("Raj", 10))

# escape characters
print("Hey, I'am a normal human being")  # won't throw error for double quotes
# use backward slash to escape
print('Hey, I\'am a normal human being uisng escape characters to print text with single quotes inbetween the text')

# existing functions to minimize the works
str3 = "capitalize me"
print(str3.capitalize())  # will capitalize the first letter of the sentences
print(str3.upper())  # will change to upper case
print(str3.lower())  # will change to lower case
print(str3.islower())
print(len(str3))    # to identify the length

str4 = " left & right space available text "
print(str4.lstrip())
print(str4.rstrip())

print(str4.find("&"))  # to find the positions of a specific characters, letters, text or string
print(str4.count("available"))  # to count the no of occurrence in a statement

# str5 = "this is to identify the minimum and maximum character" , Not clear/working properly
str5 = "abz"
print(min(str5))
print(max(str5))

str6 = "This statement is created for replace options in Python, so you may find more repeated statement"
print(str6.replace("statement", "replaced with new text"))  # replace the desired text
print(str6.split("statement"))  # to split the statement with given string

# below statement defines, how values are allocated in a array[a[]0. a[1], .....] ,
# same way, it will be allocated in negative value from the last like [a[-1], a[-2],...]
# it maintain negative indexing, which is called "slicing"
str7 = "python"
print(str7[0])
print(str7[5])
print(str7[-1])

# Comparison
str8 = "This text created to compare"
str9 = "This text created to compare"
print(str8 is str9)  # is, is used to compare the 2 values
print(str8 == str9)  # ==, is used to compare the 2 values, same as above
