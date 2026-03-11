# Write a program that: 
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run

sloveso = input("Napíš sloveso: ")
otazka = print("Viem lepšie",sloveso,"ako ty")
otazka = print("Viem lepšie " + sloveso + " ako ty")
otazka = print(f"Viem lepšie {sloveso} ako ty - fstring")
print(f"{(sloveso + " ")*5} - f string")
print((sloveso + " ")*5)
print(otazka)
