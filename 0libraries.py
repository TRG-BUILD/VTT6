""" Libraries """

"""
    Libraries are code others have written, which we can use
    They should be imported at the top, so its easy to see to others what is used, but can be imported everywhere.
"""

# statistics
print("AT STATISTICS")

# A standard library which can use basic statistical analysis
import statistics as some_st
some_data = [1, 1, 2, 3, 5, 8, 13]
print(some_st.mean(some_data))
print(some_st.median(some_data))
print(some_st.variance(some_data))

# pandas
print("AT PANDAS")
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
print("AT MATPLOTLIB")
import matplotlib.pyplot as some_plot

some_x_axis = [1, 2, 3, 4, 5]
some_y_axis = [10, 3, 7, 12, 27]
some_plot.plot(some_x_axis, some_y_axis)
some_plot.xlabel("Numbers 1 to 5")
some_plot.ylabel("Some numbers")
print("Run the command under this print statement, to show the plot")
print("The program will pause until the plot is closed, and you can save it to your computer")
#some_plot.show()

# Use the given link for a basic introduction to matplotlibs pyplot package
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html

# geopandas

# If your data contains spatial data (GPS / geometric data)
# Geopandas expands regular pandas to use this more difficult data

# Use the given link to get to know geopandas
# https://geopandas.org/index.html

# requests
print("AT REQUESTS")
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
    All kinds of SQL commands can be found here:
    https://www.w3schools.com/sql/default.asp
"""
print("AT PSYCOPG2")
import psycopg2

connect_to_database = psycopg2.connect(
    dbname="pshare",
    host="localhost",
    user="postgres",
    password="Mimtop9?"
)
cursor = connect_to_database.cursor()
# Create Table
cursor.execute("CREATE TABLE testing (column1 varchar(256), column2 varchar(256));")
# Create rows in table
cursor.execute("INSERT INTO testing (column1, column2) VALUES ('Hello', 'World');")
# Get data from table
cursor.execute("SELECT * FROM testing;")
print(cursor.fetchall())
cursor.execute("SELECT column1, column2 FROM testing;")
print(cursor.fetchall())
# Update data from table
cursor.execute("UPDATE testing SET column1='Hello Again' WHERE column2='World';")
cursor.execute("SELECT * FROM testing;")
print(cursor.fetchall())
# Delete data from table
cursor.execute("DELETE FROM testing WHERE column1='Hello Again';")
cursor.execute("SELECT * FROM testing;")
print(cursor.fetchall())
# Delete the whole table
cursor.execute("DROP TABLE testing;")

print("The above code is SQL which retrieves all data found in the vttt database.")
print("Be aware that database queries in this way affects your database, and changes")
print("are still made even after the program is finished running!")
