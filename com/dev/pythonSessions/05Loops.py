# while loop : Python has else statement in while loop, whereas Java doesn't have
# for loop : Once condition satisfy in for loop, loop comes to else loop, whereas Java doesn't have
# different way to utilize loop using range, index, len, ..
# if, nested-if

# While loop
# option 1:
print("*******************Start of while Loop 1******************************")
count = 0
while count < 3:
    print("This while loop no %d " % count)
    # print(count)
    count = count+1
print("*******************End of While Loop 1******************************")

# option 2:
print("*******************Start of while Loop 2******************************")
count = int(input("Enter the number the iterate :"))
while count < 2:
    print("You must have selected python")
    count = count + 1
else:   # added feature in Python, which is not in Java
    print("You must have selected other than python")
    count = count + 1
print("*******************End of While Loop 2******************************")

# For Loop
# You can call from list, string, etc.,

# Option 1 to iterate on no of list values
print("*******************Start of For Loop 1(no of list values)******************************")
name = ["ASP.NET", "VB", "Java", "Python"]
for i in name:  # Syntax
    print(i)
print("*******************End of For Loop 1******************************")

# Option 2 to iterate in characters in given string
print("*******************Start of For Loop 2(characters in given string)******************************")
name = "I love to learn new languages"
for i in name:
    print(i)
print("*******************End of For Loop 2******************************")

# Option 3 to iterate on range basis
print("*******************Start of For Loop 3(range basis)******************************")
name = ["ASP.NET", "VB", "Java", "Python"]
for i in range(len(name)):  # Syntax
    print(name[i])
print("*******************End of For Loop 3******************************")

# Option 4 to iterate on range basis using for loop with else
print("*******************Start of For Loop 4(range basis using for loop with else)******************************")
countrylist = ["India", "USA", "UK", "Germany"]
for i in range(len(countrylist)):  # Syntax
    print(countrylist[i])
else:
    print("countrylist is over")    # Once condition satisfy, loop comes to else loop

print("*******************End of For Loop 4******************************")

# Option 5 to up to the range basis using for loop with else
print("*******************Start of For Loop 5(up to range given using for loop with else)*****************************")
citylist = ["LeesSummit", "New York", "New Jersey", " Columbus"]
for i in range(2):  # Syntax
    print(countrylist[i])
else:
    print("citylist is over")    # Once condition satisfy, loop comes to else loop

print("*******************End of For Loop 5******************************")

# Option 6 nested for loop
print("*******************Start of For Loop 6(nested for loop)*****************************")

for i in range(1, 5):  # Syntax to iterate 1 to 5
    for j in range(i):
        print(i, end='')  # syntax to print the value, once condition satisfies and ends with space
    print()  # indent matters, tabbing of this print will change the format of output

print("*******************End of For Loop 6******************************")
