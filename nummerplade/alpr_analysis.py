# coding=utf-8
import pladelib
import argparse
import psycopg2


def clean_input(file) -> list[list[Any]]:
    """
    Open input file and remove empty frames and parse frames with input for returning af list of list
    inputs:
        file - Input file, coming from anpr-unstra
    output:
        cleaned_input - List of plates, with frame nummer aka a list(list(frame, plate))
    """

    cleaned_input = []

    return cleaned_input


def clean_plates(cleaned_input: list[list[Any]]) -> list[list[Any]]:
    """
    Check each result in cleaned_input, to see if the plate is passing our validation, Here you should use your pladelib.py library

    inputs:
        cleaned_input - List of plates, with frame nummer aka a list(list(frame, plate))
    output:
        validated -  List of plates, with frame nummer aka a list(list(frame, plate))
    """
    return validated


def get_seen_plates(validated, least_seen=4) -> list[dict[str, Any]]:
    """
    Count how many times a plate have been seen, and return plates seen enough times to accept the result

    inputs:
        validated -  List of plates, with frame nummer aka a list(list(frame, plate))
        least_seen - How many times should we have seen the plates before we accept it
    output:
        seen_plates - List of dictionaries idea with the structure: { 'plate': "AA12345" ,'count': 22, 'first_seen': 22, 'last_seen': 25}
    """


def save_to_csv(counted_plates: list[dict[str, Any]]) -> None:
    """
    Save result of seen licenseplates to file

    inputs:
        seen_plates - List of dictonaries of plates seen, and when it have been seen
    output:
        None (file as csv)
    """


def save_to_db(counted_plates: list[dict[str, Any]]) -> None:
    """
    Create connection to database, save licenseplate including the information we know.

    Table in database:
    drop table if exists alpr_clean;
    create table alpr_clean (
        plate varchar(7),
        count int,
        first_seen int,
        last_seen int
    );

    inputs:
        seen_plates - list of dictionary with plate as key, and dictionary of count, first_seen, last_seen
    output:
        None
    """
    conn = psycopg2.connect(
        dbname="vttt", host="localhost", user="postgres", password="changeme"
    )
    cursor = conn.cursor()

    # Insert statement
    for item in counted_plates:
        query = f""
        cursor.execute(query)
    else:
        conn.commit()


if __name__ == "__main__":
    """Skriv programmet, så i kan importere data fra en csv fil og gemme i en ny"""
