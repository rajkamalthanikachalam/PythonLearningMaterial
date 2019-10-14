# Data hiding is possible through encapsulation in java(Like private variable)
# Data hiding is possible through "__variable name", which is private variable
# To call it, we have to write the syntax "object._classname__privatevaaiable"
# Object Printing :
# to print the value of object reference, we have to use either str or repr method,
# str takes the priority over object printing


# Data Hiding
class Data:

    __privateVariable = 100     # Data Hiding or private variable


d1 = Data()
# print(__privateVariable)                # this will through error for not finding the variable
print(d1._Data__privateVariable)        # Syntax to access the private variable outside of class


# Object Printing
class ObjectPrinting:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "a %s : b %s" % (self.a, self.b)

    def __str__(self):
        return "Value of A is %s and Value of B is %s" % (self.a, self.b)


obj = ObjectPrinting(100, 200)
# When you call the object, this method will look for str method, if not repr method,
# else it will print the object value
print(obj)
