try:
    import numpy
    import matplotlib
    import xlrd
    import openpyxl
    import pandas
    import geopandas
    import psycopg2
    import requests

    connect_to_database = psycopg2.connect(
        dbname="vttt",
        host="localhost",
        user="postgres",
        password="changeme"
    )

    print("Alt korrekt installeret")
except Exception as e:
    print(e)
    print("\n\n")
    print("Ikke installeret korrekt. Kontakt hjælpelærer og vis den ovenstående fejl")