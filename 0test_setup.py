message = ""

try:
    import numpy
    import matplotlib
    import xlrd
    import openpyxl
    import pandas
    import geopandas
    import psycopg2
    import requests
except ModuleNotFoundError as e:
    message += "Se på 'Python 3.x' allerneders i højre hjørne, hvor x er et tal.\n"\
    message += "Den findes lige nede til venstre for 'Event Log', i nedre højre hjørne\n"
    message += "Hvis der står 'Python 3.9 (vttt)' er conda sat korrekt til Pycharm.\n"
    message += "Hvis der ikke står det, så tryk på den og vælg 'Add Interpreter'\n"
    message += "Et nyt vindue åbner op, hvor du skal trykke på 'Conda Environment'\n"
    message += "Vælg knappen 'Existing environments', og led efter den der hedder vttt\python.exe\n"
    message += "HUSK at tryk på 'Make available to all projects'\n"
    message += "Tryk ok\n"
    message += "\n"
    message += "Genkør programmet, og hvis denne besked stadig er der, kontakt da hjælpelæren."

try:
    connect_to_database = psycopg2.connect(
        dbname="vttt",
        host="postgres",
        user="postgres",
        password="changeme"
    )
except Exception as e:
    # Except connection error, give message
    message += "Databasen er ikke sat op korrekt.\n"
    message += "Prøv at gøre X"
except NameError as e:
    message += ""

if message == "":
    message += "Alt korrekt installeret"

print(message)