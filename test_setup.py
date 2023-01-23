#!/usr/bin/python
# -*- coding: WINDOWS-1252 -*-
from sys import platform

def print_system_commands(win: str, other: str) -> None:
    if platform.startswith('win'):
        print(win)
    else:
        print(other)

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
    print("Fejl besked:")
    print(e)
    print("\n\n")

    print("Bud på løsninger")
    if "No module named" in str(e):
        print(f"""Installer de manglende pakker med pip install {e.name}""")

    if 'role "postgres" does not exist' in str(e):
        print("Brugeren blev ikke korrekt opsat under installationen")
        print_system_commands("""Start din 'Anaconda Promt (miniconda3)'
                   conda activate build
                   createuser -P -s -e postgres""", """Start din terminal
                   conda activate build
                   createuser -P -s -e postgres""")

    if "Connection refused" in str(e):
        print("databasen er ikke startet")

        print_system_commands("""Start din 'Anaconda Promt (miniconda3)'
                conda activate build
                pg_ctl -D %USERPROFILE%\pgdatabase -l logfile start""",
        """Start din terminal
                conda activate build
                pg_ctl -D ~/pgdatabase -l logfile start""")

    print("Virker det ikke? Kontakt underviser og vis den ovenstående fejl")
