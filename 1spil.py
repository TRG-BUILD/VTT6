"""
    I denne opgave får du mulighed for at udvikle spillet Hangman

    1. Prøv at kør filen og gæt ordet ved at skrive i terminalen. Husk den er case sensitive! (a != A)
    2.
"""

secret_word = "SecretWord"
game_on = True

while game_on:
    guess = input("Guess a word, write here!")

    if guess == secret_word:
        game_on = False
    else:
        print("Wrong guess, try again!")


print("You guessed the word!")

