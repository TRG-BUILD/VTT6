"""
    I denne opgave går det ud på at lave et simpelt hangman spil.

    Det færdige spil går ud på, at en person aktivere hangman filen, skriver et hemmeligt ord, og så skal en anden person gætte det.
    Spillet bliver gradvist udbygget efter hver opgave.

    For at få input fra en bruger, bruges input() funktionen.
    Det der sættes imellem parenteserne (dens parameter) er den tekst der vises, mens det der tastes ind i terminalen, 
    returneres af input() som datatypen String.
    Strengen '\n' angiver 'new line', og angiver en ny linje når noget printes til terminalen.

    Løs de følgende opgaver:
    1: Kør filen, og få programmet til at printe "You guessed correctly!"
    2: Omskriv koden, så du kan vælge hvilket ord man skal gætte på.
    3: Omskriv koden, så den bruger et while loop der venter på man gætter rigtigt. 
        (HUSK at Ctrl-C altid bryder ud af koden, i tilfælde af i laver et uendeligt loop!)
    4: Omskriv koden, så man kun har et max antal gæt, før man taber. Vis hvor mange gæt man har tilbage, til brugeren som gætter.
    5: Lav en liste af de gæt som brugeren har gættet på tidligere, og vis det sammen med hvor mange gæt man har tilbage, efter hvert gæt.
    6: Hvis brugeren indsætter 1 bogstav, brug find() funktionen for at vise til brugeren hvor bogstavet findes i ordet. 
        Lav det gerne som en seperat funktion.
    7: Opret en variabel, som viser hvad brugeren har gættet rigtigt (som i almindelig Hangman, eks. "h_ll_" i tilfælde af hello)
    Ekstra opgaver
    8: Hvordan kan koden omskrives til at a og A bliver anset som gæt på samme bogstav? (hint: lower() eller upper() funktionen) 
    9: Hvordan kan koden omskrives til at bruge et for loop istedet for et while loop? (hint: range() funktionen)
    10: Hvordan kan koden omskrives til at man angiver en bruger og gætter først, og holder styr på point imellem runder?
    11: Hvordan kan koden omskrives til at bruge funktioner?
    12: Andre udvidelser du selv kunne forestille dig?
"""

correct_word = "Hello"

guess_word = input("Guess a word!\n")

if guess_word == correct_word:
    print("You guessed correctly!")
else:
    print("You guessed incorrectly")