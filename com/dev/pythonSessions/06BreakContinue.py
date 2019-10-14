# break & continue key word, helps to continue or break the statement from the loop

# Break for String
string = "LiveAndLetLive"
for index in string:
    print(index)
    if index == "A":
        print("Breaking the Loop once reaches A")
        break

# Continue for String
string = "LiveAndLetLive"
for index in string:
    print(index)
    if index == "A":
        print("Continuing the Loop even after reaching A")
        continue  # without continue also loop will reach reach end
print("End of Loop")

# for list with array index(without range)
string = ["Live", "And", "Let", "Live"]
for index in string:
    print(index)
    if index == "And":
        print("Breaking the Loop once reaches A")
        break

# for list with Range
string = ["Live", "And", "Let", "Live"]
for index in range(len(string)):    # good to use range when for loop is used
    print(string[index])
    if string[index] == "And":
        print("Breaking the Loop once reaches And")
        break

# setting flag for loop
string = ["Live", "And", "Let", "Live"]
Flag = False
print("Flag set to False")
for index in range(len(string)):    # good to use range when for loop is used
    print(string[index])
    if string[index] == "And":
        Flag = True
        if Flag.__eq__(True):
            print("Flag set to True")
        break
