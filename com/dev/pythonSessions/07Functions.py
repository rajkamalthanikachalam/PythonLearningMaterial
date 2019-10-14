# Function: a piece of code to execute a repeated functions
# Recursion: A function calling itself
# Arguments : *arg is used to pass a single arguments
# Key words : **args is used to pass a multiple arguments in key & value format
# Lambda functions : Anonymous functions or function without name

# Function


def function(username):
    print(username)


function(username="test1")


def function(username, password):
    print(username, password)


function("user1", "test123")                    # You can pass arguments in both way
function(username="user1", password="test123")  # You can pass arguments in both way


# Functions with no arguments


def function1():  # syntax to define a function
    print("My First Function with no argument")


function1()

# Functions with single arguments


def function2(a):
    print("Function with single argument : %d" % a)
    return function2


function2(100)

# Functions with two arguments and return


def function3(a, b):
    c = a+b
    print("Function with two arguments : %d" % c)
    return c


function3(10, 15)


# Functions with default/Optional parameter

def function4(name="None Selected"):
    print(name)


function4()
function4("India")
function4("Australia")


# Functions with List

def function5(name):
    for index in name:
        print(index)


countryName = ["India", "Australia", "Africa", "America"]
function5(countryName)


# Functions with if- Else statement

def function6(country_name):
    if country_name == "India":
        print("Capital is New Delhi")
    elif country_name == "Australia":
        print("Capital is Melbourne")
    elif country_name == "Africa":
        print("Capital is Cape Town")
    elif country_name == "America":
        print("Capital is Washington DC")
    else:
        print("Not in the list")


function6("China")


# Recursion : Function calling itself , ie factorial of 5 (5*4*3*2*1)

def recursion(num):
    if num > 1:
        num = num * recursion(num-1)
    return num


print(recursion(5))


# Arguments
print("********************************Arguments**************************************")


def arguments(*arg):
    for x in arg:
        print(x)


arguments(10, 12, 15, 18, 19)
arguments("Maths", "Science", "History", "English")

print("********************************Key word Arguments**************************************")
# **args is syntax
# for key, value in args.items(): is syntax


def arguments(**args):
    for key, value in args.items():
        print("%s == %s" % (key, value))


arguments(user1="test1", user2="test2", user3="test3")
arguments(xyz=10, abc=20, ijk=30)


# Lambda
# syntax lambda x: define the function after colon
print("********************************Lambda**************************************")

cube = lambda n: n*n*n


cubeX = cube(4)
print("Cube of C is  %d" % cubeX)

total = lambda mark: mark+30


sumTotal = total(150)
print("Total mark earned is %d" % sumTotal)
