"""
    I denne opgave skal der udvikles et lille bibliotek der hjælper med at filtrere nummerplader
    og tjekke hvis de passer til dansk format. 
"""


def is_format_ok(plate):
    """
    check whether the plate corresponds to the correct format
    """
    # YOUR SOLUTION GOES HERE
    return False


def is_length_ok(plate):
    """
    check whether the length of the plate is according to the rules
    """
    # YOUR SOLUTION GOES HERE
    print("hej", plate)
    return False


def is_plate_ok(plate):
    """
    check whether plate has both length and format correct
    """
    # YOUR SOLUTION GOES HERE
    return False


def check_plate(plate):
    """
    check plate and output results
    """
    # YOUR SOLUTION GOES HERE
    print("Sir, i don't know...")


def main():
    """
    This function will be called if and only if user
    calls python pladelib.py from CLI
    """
    import argparse

    # get numberplate from a command line
    parser = argparse.ArgumentParser(description="Validate number plates")
    parser.add_argument(
        "-p", "--plate", type=str, required=True, help="numberplate to be checked"
    )
    args = parser.parse_args()

    # print check result
    check_plate(args.plate)


if __name__ == "__main__":
    main()
