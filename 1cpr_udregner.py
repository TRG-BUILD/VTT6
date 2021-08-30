"""
    I denne introducerende opgave skal i udregne det sidste ciffer i jeres CPR nummer.
    Indtil 2007 brugte man en metode til at vurdere, om et CPR nummer er validt.
    Ud fra de første 9 cifre i CPR nummeret, kan man udregne det sidste tiende ciffer.

    Regnestykket er at man ganger alle ens første 9 cifre med nogle tal, lægger alle værdierne sammen,
    udregner den tilbageværende rest efter en division med 11, og tager til sidst 11
    og trækker rest værdien fra.
    Dette er så ens tiende ciffer, og processen kan automatiseres med python,
    så i kan tjekke om alle jeres familiemedlemmers CPR numre nu også er valide.

    Dette gøres ud fra denne tabel:
    Ciffer:         1  2  3  4  5  6  7  8  9
    Multiplikator:  4  3  2  7  6  5  4  3  2

    Et eksempel:
    Regnestykket bliver således for en person født 11. januar 1950, som har 123 efterfølgende
    (CPR: 110150 123X, hvor X er det tiende ciffer):
    (1 * 4)  +  (1 * 3)  + (0 * 2)  + (1 * 7)  + (5 * 6) + (0 * 5) + (1 * 4) + (2 * 3) + (3 * 2)
    = 5 + 3 + 0 + 7+ 30 + 0 + 4 + 6 + 6
    = 61
    Dette tal divideres så med 11, hvor man får resten.
    61 % 11 = 6
    Man tager så til sidst 11 - rest tallet (11 -6 = 5), hvilket giver det endelige ciffer.
    CPR: 110150 123X -> 110150 1235

    Denne udregning gælder for alle valide CPR numre før 2007, og i kan dermed tjekke jeres eget CPR.

    I skal herunder skrive et python program der laver den udregning.
    Der bliver stillet 5 opgaver, hvor i gradvist udbygger jeres algoritme. Lav opgaverne i rækkefølge.
    Se i "0oversigt.py" filen, for en hurtig reference.

    1: Ved brug af basale datatyper og variable, lav udregningen for dit CPR nummer, og print det tiende ciffer.
    2: Gem dit CPR nummer som en streng i en variabel, og brug den istedet for.
    3: Brug lister til at repræsentere multiplikationstabellen og loops til at gå gennem den
    4: Brug conditionals til at udregn det tiende ciffer hvis kun et 9 ciffer CPR er givet,
        og ellers vurdere om et CPR nummer er validt, hvis 10 cifre er givet.
    5: Omdan den kode du har lavet til en funktion, som tager et 9 eller 10 ciffer CPR nummer ind som parameter.

    Sammenlign koden på tværs af hinanden, og afprøv den evt. på folk du kender
"""