# coding=utf-8
import pladelib
import argparse


def clean_input(file):
    """
    Open input file and remove empty frames and parse frames with input for returning af list of list
    inputs:
        file - Input file, coming from openALPR
    output:
        cleaned_input - List of plates, with frame nummer aka a list(list(frame, plate)) 
    """

    cleaned_input = []

    return cleaned_input


def clean_plates(cleaned_input):
    """
    Check each result in cleaned_input, to see if the plate is passing our validation, Here you should use your pladelib.py library

    inputs:
        cleaned_input - List of plates, with frame nummer aka a list(list(frame, plate))
    output:
        validated -  List of plates, with frame nummer aka a list(list(frame, plate))
    """
    return validated


def get_seen_plates(validated, least_seen=4):
    """
    Count how many times a plate have been seen, and return plates seen enough times to accept the result

    inputs:
        validated -  List of plates, with frame nummer aka a list(list(frame, plate))
        least_seen - How many times should we have seen the plates before we accept it
    output:
        seen_plates - Dictionary idea for scructure: seen_plates['AA12345'] = { 'count': 22, 'first_seen': 22, 'last_seen': 25}
    """


def save_to_csv(output):
    """
    Count how many times a plate have been seen, and return plates seen enough times to accept the result

    inputs:
        seen_plates - Dictonary of plates seen, and when it have been seen
    output:
        None (file as csv)
    """


if __name__ == "__main__":
    """Skriv programmet, så i kan importere data fra en csv fil og gemme i en ny"""
