# A single-line comment (Comments are never run in the code!)
"""
    A multi-line
    comment
    ALL names with "some" in it, means it is an arbitrary name which you yourself use
    (But has to use consistently, with no typing errors!)
    All other names are python syntax, ie. python code language which is used to write a program.
"""

""" DataTypes """

# Strings
"This is a string"
print("Strings can be printed to the terminal")
print("Everything inside the parentheses will be written, if its a string")
print("Strings can be " + "concatenated " + " which means put together from multiple strings")

# Numbers
print("To print numbers, you need to convert it to a string: " + str(1234))
print("Addition: " + str(5 + 5))
print("Subtraction" + str(5 - 5))
print("Multiplication " + str(5 * 5))
print("Division " + str(5 / 5))
print("Modulo (keeping the remainder of a division) " + str(5 % 5))

# Bools
print("Bools are values that are either ", True, " or ", False)
print("Equality: ", 5 == 5)
print("Equality: ", "Hello" == "Hello")
print("Comparison", 5 > 10)
print("Comparison", 5 <= 5)

""" Data Structures """

# Variables
# The right hand side gets evaluated to a datatype with a specific value, and then assigned to the variable
some_variable = "Hello"
print("First the variable has a value of: " + some_variable)
some_variable = "Farewell"
print("Then, it is changed into something else: ", some_variable)
print("Individual characters in a string can also be accesed")
print(some_variable[0], " This prints an 'F', and ", some_variable[1], " prints an 'a'")
print("All accessing this way always start at 0, aka. the first element has the 0 index")

# Lists
print([0, 1, 2, 3, 4])
print("Lists are collections of objects, aka. strings, numbers, bools or even other lists!")
some_list = ["Hello", 123, True, ["This", "Is", "A", "New", "List"], 321]
print("The first element in a list is: ", some_list[0])
print("The last element in a list is: ", some_list[-1])
print("To add an element to the end: ", some_list.append("A new item after 321"))
print("To add an element to front ", some_list.insert(0, "A new item before Hello"))
print("To remove an element ", some_list.remove("Hello"))

# Dictionaries
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
if(False):
    print("Don'tDoThis")
elif(True):
    print("DoThis")
elif(True):
    print("This won't happen, since the previous if statement is true")
else:
    print("If everything fails, do this")

# Loops
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
print("Functions define mini programs, that can be run when called (see line 106)")
print("Functions also have parameters, which are variables that get copied into the function")


def some_func_name_you_choose(some_parameter_name, some_other_parameter_name):
    print(some_other_parameter_name)
    print(some_parameter_name)
    return some_other_parameter_name + some_parameter_name


some_variable = some_func_name_you_choose("World!", "Hello ")
print("some_func_name_you_choose will execute, then return its value, assigning it to some_variable")
print("some_variable will give the output of: " + some_variable)

"""Some useful functions"""
length_of_something = len([0, 2, 4, 6, 8, 10])
print("Has a length of: ", length_of_something)
length_of_something = len("Hello World!")
print("Has a length of: ", length_of_something)


""" Libraries """

# pandas
import pandas as some_pd

some_dictonary = {
    "Column1": ["Item1Row1", "Item5Row2", "Item9Row3"],
    "Column2": ["Item2Row1", "Item6Row2", "Item10Row3"],
    "Column3": ["Item3Row1", "Item7Row2", "Item11Row3"],
    "Column4": ["Item4Row1", "Item8Row2", "Item12Row3"]
}

some_dataframe = some_pd.DataFrame(some_dictonary)
print("Printing the whole dataframe")
print(some_dataframe)
some_dataframe.index = ["First", "Second", "Third"]
print("Showing the changed index")
print(some_dataframe)
print("Indexing from the second row up to but not including the fourth row")
print(some_dataframe[1:4])
print("Getting the first rows, either through the named index, or by looking for the first element")
print(some_dataframe.loc["First"])
print(some_dataframe.iloc[0])
print("Getting multiple rows, by passing a list of index names instead")
print(some_dataframe.loc[["First", "Second"]])
print("Getting a single label, by passing an index and a column")
print(some_dataframe.loc["First", "Column2"])
print("Importing from Comma Seperated Files (.csv) instead")
print("decimal=',' gives danish decimal notation, and headers gives the column names")
some_column_names = ["Id", "Manufactor", "Model", "Drivmiddel", "KmPrÅr", "Årgang"]
some_car_data = some_pd.read_csv("dataset/bil_import.csv", decimal=",", sep=";", names=some_column_names)
print(some_car_data[100:130])
print("Show some descriptions of the data")
print(some_car_data.describe())

# Use the given link for a basic introduction to pandas:
# https://www.learnpython.org/en/Pandas_Basics

# matplotlib
import matplotlib.pyplot as some_plot

# Use the given link for a basic introduction to matplotlibs pyplot package
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html

# geopandas

# If your data contains spatial data (GPS / geometric data)
# Geopandas expands regular pandas to use this more difficult data

# Use the given link to get to know geopandas
# https://geopandas.org/index.html

# requests
import requests
"""
    We can access websites through requests, and special websites (called APIs)
    makes it possible for us to retrieve data as dictionaries.
    Here is an example of retrieving data from Oluf Borchs Vej
    You can access ALL data from https://dawa.aws.dk to use in your projects!!!
"""
some_payload = {'postnr': 9000, 'vejnavn': 'Oluf Borchs Vej'}
some_response = requests.get('https://dawa.aws.dk/adresser', params=some_payload)

# The data is in json format (an internet standard), so have to be convertedd to a dictionary in python
some_dictionary_data = some_response.json()

# We can also directly see the url which can be copy/pasted into a browser
print(some_response.url)

# psycopg2

"""
    If you want to interact with your database through python programming,
    You can use the psycopg2 package
"""
import psycopg2

connect_to_database = psycopg2.connect(
    dbname="vttt",
    host="localhost",
    user="postgres",
    password="changeme"
)
cursor = connect_to_database.cursor()
cursor.execute("SELECT * from vttt")
print("The above code is SQL which retrieves all data found in the vttt database.")
print("Be aware that database queries in this way affects your database, and changes")
print("are still made even after the program is finished running!")