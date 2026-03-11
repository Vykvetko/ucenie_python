# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints a bool depending on whether the guess matches the secret.

tajne_cislo = 9
user_cislo = int(input("Napíš čislo, ktore si myslíš že by mohlo byť tajne: "))
stav = (tajne_cislo == user_cislo)
print(stav)

