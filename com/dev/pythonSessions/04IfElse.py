a = int(input("Enter the A Value : "))          # accept only integer type, you define the required type as input
b = int(input("Enter the B Value : "))
c = int(input("Enter the C Value : "))
d = int(input("Enter the D Value : "))
e = str(input("Enter the E Value : "))

print("Value of E is %s " % e)
print("Value of A after adding 100 to it %d " % (a+100))

# if else statement
if a > b and a > c and a > d:      # we need to use and instead of && from java
    print("A is greater")
elif b > c and b > d:              # elif not else if
    print("B is greater")
elif c > d:
    print("C is greater")
else:
    print("D is greater")

# Another if conditions
if a.__ge__(b) and b.__ge__(c) and c.__ge__(d):
    print("Value of A after adding 100 is %d " % (a+100))
elif b.__ge__(c) and c.__ge__(d):
    print("Value of B after adding 100 is %d " % (b+100))
elif c.__ge__(d):
    print("Value of C after adding 100 is %d " % (c + 100))
else:
    print("Value of D after adding 100 is %d " % (d + 100))

# concatenate : concatenation of string followed by int is possible, whereas int followed by String is not possible
# option1
print("concatenate string followed by int")
concatenate1 = e+str(a)
print(concatenate1)
# print("concatenate int followed by String")
# concatenate = a+int(e)
# print(concatenate)

# option 2 for concatenate using f string like f'{}{}
concatenate2 = f'{e}{str(a)}'
print(concatenate2)
