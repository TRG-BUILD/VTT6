import pladelib

test_plader = [
    ("XX00000", True, "is correct length and format."),
    ("AB12345", True, "is correct length and format."),
    ("CD00", False, "is not correct length."),
    ("N010101", False, "has an integer in letters part."),
    ("GG11L10", False, "has a letter in integers part."),
]

for plate, isOk, reason in test_plader:
    isOkLib = pladelib.is_plate_ok(plate)
    print("{:<8} correct?: library: {:<5}, expected: {:<5}, because: {}".format(
        plate, str(isOkLib), str(isOk), reason))
