# Set objects are collection of data type
# List & tuple are order based on index, but set is not order based , it prints randomly in a set objects
# Set stores different type of data
# Its performs different mathematical operations
# It does not store duplicate elements
# To define, we need to use {}
# While creating set objects, number, strings & tuple are allowed, List & Dictionary are not allowed(Except using set)

# syntax
# Tuple = ()
# List = []
# set = {}

set1 = {1, 2, 3, 4, 5}
set2 = {"Java", "Python", "C", "ASP.Net", "VBA"}
print(set1)
print(set2)
print("Maintains no order % s" % set2)

# No duplicates allowed
set2 = {"Java", "Python", "C", "ASP.Net", "VBA", "Java", "C"}
print("No Duplicated allowed %s" % set2)

# Set allows tuple, list using key word using function set()
set1 = set([1, 2, 3, 4, 5])
set2 = set(("Java", "Python", "C", "ASP.Net", "VBA"))
print("List can be print using keyword set(): %s" % set1)
print("Tuple can be print using keyword set() : %s" % set2)

# set Object stores only Numbers, Strings, Tuple not list and dictionary
set1 = {("Java", "Python", "C"), "ASP.Net", "VBA"}
print("Set Object allows Numbers, Strings, Tuple not list and dictionary : %s" % set1)
# This will throw error because set won't allow list and dictionary
# set2 = {[1, 2], 3, 4, 5}
# print("Set Object allows Numbers, Strings, Tuple not list and dictionary : %s" % set2)

# Set Operations

# Union
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 7, 8, 5}
print(set1 | set2)            # syntax for union function : union of all
print(set1.union(set2))     # syntax for union function

# Intersection
print(set1 & set2)                # syntax for Intersection function
print(set1.intersection(set2))  # syntax for Intersection function

# Differences
print(set1 - set2)
print(set1.difference(set2))

# Symmetric differences
print(set1 ^ set2)                  # unique among the both
print(set1.symmetric_difference(set2))

# Add
set1 = {"Java", "Python", "C", "ASP.Net", "VBA"}
set1.add("New Language")
print("Add operation : %s " % set1)

# update
set1 = {"Java", "Python", "C", "ASP.Net", "VBA"}
set1.update(["Ruby", "Django"])     # Syntax to update update.([])
print("Update operation : %s " % set1)

# Clear
set1.clear()
print("Clear Operation : %s" % set1)

# Copy
set1 = {"Java", "Python", "C", "ASP.Net", "VBA"}
set2 = set1.copy()
print("set Copy is %s" % set2)

# Discard
set1 = {"Java", "Python", "C", "ASP.Net", "VBA"}
set1.discard("Java")    # Discard wont throw error for unknown value but remove does
print("Discard operation without Duplicate %s" % set1)
set1.discard("Raj")     # Discard wont throw error for unknown value but remove does
print("Discard operation with Duplicate %s" % set1)

# Remove
set1 = {"Java", "Python", "C", "ASP.Net", "VBA"}
set1.remove("C")
# set1.remove("C", "Raj")    # Discard wont throw error for unknown value but remove does
print("Remove Operation %s" % set1)
