# A single-line comment (Comments are never run in the code!)
"""
    A multi-line
    comment
    ALL names with "some" in it, means it is an arbitrary name which you yourself use
    (But has to use consistently, with no typing errors!)
    All other names are python syntax, ie. python code language which is used to write a program.
"""

""" DataTypes """

#    All Datatypes, Datastructures and functions are objects.
#    An object is something which is saved in memory, when the program runs, and is then cleaned up.
#    Objects also have access to methods, which is signified by the use of .some_method_name after the object.

# Strings
print("AT STRINGS")
"This is a string"
print("Strings can be printed to the terminal")
print("Everything inside the parentheses will be written, if its a string")
print("Strings can be " + "concatenated " + " which means put together from multiple strings")
print("You can also make strings using 'these' inside")
print('Python doesnt care whether its single quote or double quote (like these """) ')
print("You can find where a given word starts in a string with the find method")
print("The word Hello occurs at the 5. place in this: ", "Well Hello There!".find("Hello"))

# Numbers
print("AT NUMBERS")
print("To print numbers, you need to convert it to a string: " + str(1234))
print("Addition: " + str(5 + 5))
print("Subtraction" + str(5 - 5))
print("Multiplication " + str(5 * 5))
print("Division " + str(5 / 5))
print("Modulo (keeping the remainder of a division) " + str(5 % 5))

# Bools
print("AT BOOLS")
print("Bools are values that are either ", True, " or ", False)
print("Equality: ", 5 == 5)
print("Equality: ", "Hello" == "Hello")
print("Comparison", 5 > 10)
print("Comparison", 5 <= 5)

""" Data Structures """

# Variables
print("AT VARIABLES")
# The right hand side gets evaluated to a datatype with a specific value, and then assigned to the variable
some_variable = "Hello"
print("First the variable has a value of: " + some_variable)
some_variable = "Farewell"
print("Then, it is changed into something else: ", some_variable)
print("Individual characters in a string can also be accesed")
print(some_variable[0], " This prints an 'F', and ", some_variable[1], " prints an 'a'")
print("All accessing this way always start at 0, aka. the first element has the 0 index")

# Lists
print("AT LISTS")
print([0, 1, 2, 3, 4])
print("Lists are collections of objects, aka. strings, numbers, bools or even other lists!")
some_list = ["Hello", 123, True, ["This", "Is", "A", "New", "List"], 321]
print("The first element in a list is: ", some_list[0])
print("The last element in a list is: ", some_list[-1])
print("To add an element to the end: ", some_list.append("A new item after 321"))
print("To add an element to front ", some_list.insert(0, "A new item before Hello"))
print("To remove an element ", some_list.remove("Hello"))

# Dictionaries
print("AT DICTIONARIES")
some_dictonary = {"key1": "value1", "key2": "value2", "key3": 123}
print("Dictionaries are pairs of keys and values")
print("You can access a value through its key: ", some_dictonary["key1"])
print("You can change a value through its key")
some_dictonary["key2"] = "A new value"
print("You can add new key value pairs")
some_dictonary["ATotallyNewKey"] = "A New Value"
print(some_dictonary)

""" Control Structures """

# Conditions
print("AT CONDITIONS")
if(False):
    print("Don'tDoThis")
elif(True):
    print("DoThis")
elif(True):
    print("This won't happen, since the previous if statement is true")
else:
    print("If everything fails, do this")

# Loops
print("AT LOOPS")
# For loop
for some_name_you_choose in [0, 1, 2, 3, 4]:
    print(some_name_you_choose)
print("This will print 0,1,2,3,4 on each seperate line")

for index, some_name_you_choose in enumerate([10, 20, 30, 40]):
    print(index, " , ", some_name_you_choose)
print("This will print 0 , 10   1 , 20   2 , 30   3 , 40")

# While loop
condition = 5
while condition != 0:
    print(condition)
    condition -= 1
print("This will print 5,4,3,2,1 (but not 0)")
print("Beware! These can make infinite loops (try to remove condition -= 1")

# Functions
print("AT FUNCTIONS")
print("Functions define mini programs, that can be run when called (see line 106)")
print("Functions also have parameters, which are variables that get copied into the function")


def some_func_name_you_choose(some_parameter_name, some_other_parameter_name):
    print(some_other_parameter_name)
    print(some_parameter_name)
    return some_other_parameter_name + some_parameter_name


some_variable = some_func_name_you_choose("World!", "Hello ")
print("some_func_name_you_choose will execute, then return its value, assigning it to some_variable")
print("some_variable will give the output of: " + some_variable)

"""Some useful functions and trivia"""
print("AT USEFUL FUNCTIONS")
length_of_something = len([0, 2, 4, 6, 8, 10])
print("Has a length of: ", length_of_something)
length_of_something = len("Hello World!")
print("Has a length of: ", length_of_something)
some_data = [1, 2, 3, 4]
sum_of_something = sum(some_data)
print("The total sum of it all is: ", sum_of_something)
print("The max value is: ", max(some_data))
print("The min value is: ", min(some_data))
some_range_of_numbers = range(5)
print("This gives a range of numbers: ", some_range_of_numbers)
some_defined_range = range(3, 7)
print("This gives a range not starting from 0: ", some_defined_range)