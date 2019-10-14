# object is the super class of all class, when you define in class arguments
# Multiple Inheritance is possible , i.e., child can access 2 parent class at a same time,
# which is not possible through java
# Child class can access parent class members( in child class, use parent class name. variable")
# Multiple Inheritance is allowed on python


class SuperClass(object):

    def __init__(self, name):
        self.name = name
        print("This is super class method")

    def get_name(self):
        return self.name

    def is_employee(self):   # Method overriding : Parent and child share the same method name with same arguments
        return False


class SubClass(SuperClass):          # syntax to call super class in child class

    def __init__(self, name):
        self.name = name
        print("This is sub class method")

    def is_employee(self):   # Method overriding : Parent and child share the same method name with same arguments
        return True


parent = SuperClass("Raj Kamal")
print(parent.get_name())
print(parent.is_employee())

child = SubClass("Raj Kamal Thanikachalam")
print(child.get_name())      # Calling parent class methods through child class reference object
print(child.is_employee())   # Calling parent class methods through child class reference object
print("*********************How to find the parent class using keywords ********************************")


class Base(object):
    pass    # way of creating a empty class


class Child(Base):
    pass


print(issubclass(Child, Base))  # issubclass:  is the keyword to find the subclass connection
print(issubclass(Base, Child))

b = Base()
c = Child()
print(isinstance(b, Base))  # isinstance: is the keyword to find the instance of classes
print(isinstance(c, Base))
print(isinstance(b, Child))
print("***************************************Multiple Inheritance***********************************")


class Parent1(object):          # Parent Class 1

    def __init__(self):
        self.x = "ParentA"
        print("This is Parent Class A")


class Parent2(object):          # Parent Class 2

    def __init__(self):
        self.y = "ParentB"
        print("This is Parent Class B")


class Child(Parent1, Parent2):    # Multiple Inheritance, calling 2 parent class at a same time

    def __init__(self):
        Parent1.__init__(self)  # way to call parent class in child class using " parent class.__init__()"
        Parent2.__init__(self)
        print("This is Child Class which inherit the Parent class A & B at same time")

    def get_string(self):
        print(self.x, self.y)


ch = Child()
print(ch.get_string())
print("*****************************How to access Parent member from child class*********************************")


class BaseClass(object):

    def __init__(self, x):
        self.x = x
        print("Value of X is %s" % x)


class SubClass(BaseClass):

    def __init__(self, x, y):       # syntax to call parent class member
        BaseClass.x = x             # syntax to call parent class member
        self.y = y

    def get_string(self):
        print("Value of Base class member : %s" % BaseClass.x)
        print("Value of child class member : %s" % self.y)


sc = SubClass(10, 20)
print(sc.get_string())
