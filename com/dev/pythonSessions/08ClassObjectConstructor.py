# CLASS*******************************************************
# Class : To create a class "class" keyword will be used in python file
# N no of class can be created in same python file
# blank class creation is possible
# Multiple object can be created for single class
# Calling class variable can be done through 2 ways, creating object and directly through class name
# self in arguments are default, no need to define them, which means will pass 0 to it
# Self represents, current class(like this in java)
# Any variable defined inside the method/constructor is called instance variable
# Sequence of method calling is important

# CONSTRUCTOR*************************************************
# Constructor syntax : def __int__(self):
# Constructor overloading is not possible
# latest constructor will be picked


class Test:
    # Class Variable, which is not public or private variable
    NoOfWheels = 4
    DefaultColor = ""

    # Constructor without arguments
    def __init__(self):       # syntax for calling constructor
        self.ForConstructor = "White"
        print("Value of default constructor color is %s" % self.ForConstructor)

    # Constructor can be pass with multiple arguments, though latest constructor will be picked
    # Constructor with arguments is not working
    def __init__(self, color):
        self.color = color
        print("Value of parameterized constructor color is %s" % self.color)

    # Method
    # Any variable defined inside the method/constructor is called instance variable
    def set_price(self, price):
        self.price = price
        print("Price value is %d" % price)

    def get_price(self):
        return self.price


# Calling class variable can be done through 2 ways, creating object and directly through class file
# C1 = Test()  # Calling class method and default constructor
C1 = Test("Red")   # For Parameterized constructor
print("Calling class Variable with object : %d" % C1.NoOfWheels)
print("Calling class Variable with class name : %d" % Test.NoOfWheels)
C1.set_price(1254)  # Calling class methods
print(C1.get_price())

# another class can be written in same in file
# simple Addition program


class Calculation:

    x = " "
    y = " "

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Value of X is %d " % self.x)
        print("Value of X is %d " % self.y)

    def add(self):
        print("Addition : %d" % self.addition)

    def sub(self):
        print("Subtraction : %d" % self.subtraction)

    def mul(self):
        print("Multiplication : %d" % self.multliplication)

    def div(self):
        print("Division : %d" % self.division)

    def cal(self):
       self.addition = self.x + self.y
       self.subtraction = self.x - self.y
       self.multliplication = self.x * self.y
       self.division = self.x / self.y


c2 = Calculation(10, 5)     # Sequence of method calling is important
c2.cal()
c2.add()
c2.sub()
c2.mul()
c2.div()
