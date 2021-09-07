"""
    Denne fil giver et overblik over de mest almindelige fejl.

    The most common error is "Syntax Error", which means you have written something wrong.
    Its either at the line which the Syntax Error says, or the line before it typically (a missing comma / letter are the usual errors)
"""

try:
    some_var1 = 5
    some_var2 = "5"
    some_number = some_var1 + some_var2
except TypeError as some_e:
    print(some_e)
    print("You can't put different data types together")
    print("You need to make a conversion, like: ", 5 + int("5"))
    print("Or this: ", str(5) + "5")

try:
    some_dictionary = {"1": "One"}
    some_dictionary.append({"2": "Two"})
except AttributeError as e:
    print(e)
    print("The object does not have the given attribute/method (some_dictionary.some_method_or_attribute)")

try:
    import pandas as some_pd
    some_dictonary = {
        "Column1": ["Item1Row1", "Item5Row2", "Item9Row3"],
        "Column2": ["Item2Row1", "Item6Row2", "Item10Row3"],
        "Column3": ["Item3Row1", "Item7Row2", "Item11Row3"],
        "Column4": ["Item4Row1", "Item8Row2"]
    }
    some_dataframe = some_pd.DataFrame(some_dictonary)
except ValueError as e:
    print(e)
    print("The DataFrame needs a complete Rectangle to be loaded in")
    print("If some data is missing, you need to insert '' or similar")