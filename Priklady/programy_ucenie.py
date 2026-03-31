
## SHIFT + ALT + V - PRIDANIE / ODOBRATIE komentu 
# Priradenie klavesy
# vo VS Code -> File -> Preferences -> Keybord Shorcuts -> Toggle Line Comment

## Write a program that: 
# Asks the user for a verb.
# Prints "I can _ better than you" where you replace _ with the verb.
# Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run

# sloveso = input("Napíš sloveso: ")
# otazka = print("Viem lepšie",sloveso,"ako ty")
# otazka = print("Viem lepšie " + sloveso + " ako ty")
# otazka = print(f"Viem lepšie {sloveso} ako ty - fstring")
# print(f"{(sloveso + " ")*5} - f string")
# print((sloveso + " ")*5)
# print(otazka)


## Program na vyrátanie jednej tretiny ČISLA

# tretina = 1/3
# moje_cislo = int(input("Vlozime cislo, ktorého 1/3 chceme zobraziť: "))
# print(f"{tretina*moje_cislo:.2f} je {tretina*100:.2f}% (1/3) z {moje_cislo}")


## Newtonova metoda 
# matematický algoritmus, ktorý postupne opravuje počiatočný odhad
# na zaklade chyby (rozdiel medzi g³ a x) vypočíta lepší odhad, až kým sa nepriblíži k správnemu výsledku.

# x = int(input('Akému čislu treba vyrátať KOREŇ tretej odmocniny:  '))
# odhad = float(input('Aký je náš odhad (aká bude tretia odmocnica) ')) 
# print('Tretia mocnina našho odhadu = ', odhad**3)
# dalsi_odhad = odhad - ((odhad**3 - x)/(3*odhad**2))
# print('Dalši odhad = ', dalsi_odhad)


## Pribeh so ZOO
# práca s premennami a user inputom

# nazov_mesta1 = input("Vloz nazov mesta: ")
# osoba1 = input("Napis meno znameej/neznamej osoby: ")
# vlastnost1 = input("Napis ako vyzerala osoba predtym: ")
# zamestnanie1 = input("Napis cim sa ziví osoba predtým: ")
# vlastnost2 = input("Napis ako som sa ja vtedy citil: ")

# print(f"Dneska som bol v ZOO v meste, ktoré sa volá {nazov_mesta1}")
# print(f"Medzi navštevníkmi som uvidel {osoba1}")
# print(f"Táto {osoba1} bola {vlastnost1} a pracuje ako {zamestnanie1}")
# print(f"Ja som sa v ten den citil {vlastnost2}")


## Write a program that:
# Saves a secret number. 
# Asks the user for a number guess.
# Prints whether the guess is too low, too high, or the same as the secret. 

# tajne_cislo = 5
# odhad = int(input("Ake odhadujeme cislo: "))

# if tajne_cislo == odhad:
#     print("Trafil si tajne cislo")
# elif tajne_cislo > odhad:
#     print("Tvoj odhad je slaby")
# else:
#     print("Tvoj odhad bol priliš vysoky")
# print(f"Tajne čislo bolo: {tajne_cislo} a tvoj odhad bol: {odhad}")


## Write a program that:
# Saves a secret number. 
# Asks the user for a number guess.
# Prints a bool depending on whether the guess matches the secret.

# tajne_cislo = 9
# user_cislo = int(input("Napíš čislo, ktore si myslíš že by mohlo byť tajne: "))
# stav = (tajne_cislo == user_cislo)
# print(stav)


## Kalkulačka

# znamienko = input("Zadaj znamienko matematickej operácie, ktorú chceme vykonať (+ - / *): ")
# cislo1 = float(input("Zadaj prve cislo: "))
# cislo2 = float(input("Zadaj druhé cislo: "))

# if znamienko == "+":
#     print(f"Vysledok scitania nasich cisel je: {cislo1 + cislo2} ")
# elif znamienko == "-":
#     print(f"Vysledok odcitania nasich cisel je: {cislo1 - cislo2} ")
# elif znamienko == "*":
#     print(f"Vysledok nasobenia nasich cisel je: {cislo1 * cislo2} ")
# elif znamienko == "/":
#     print(f"Vysledok delenia nasich cisel je: {cislo1 / cislo2} ")
# else:
#     print("Zle zadané hodnoty")


## Váhový konvertor

vaha = float(input("Zadaj svoju váhu: "))
jednotky = input("Vyber jednotky ci váha je v KG alebo v LIBRACH (K alebo L): ")

if jednotky == "K": 
    print(f"Tvoja váha v librách je: {vaha * 2.205}") # keďze sme vybrali moznosť K (ako kg) => musime konvertovať kg na libry 
elif jednotky == "L":
    print(f"Tvoja váha v kilách je: {vaha / 2.205}")
else:
    print("Zadal si nesprávnu volbu")

# # 2.sposob
if jednotky == "K": 
    vaha = vaha * 2.205
    jednotky = "LBS"
elif jednotky == "L":
    vaha = vaha / 2.205
    jednotky = "KG"
else:
    print("Zadal si nesprávnu hodnotu do VAHY alebo JEDNOTIEK!")
print(f"Tvoja váha je {round(vaha,1)} {jednotky}")


## Teplotny konvertor

teplota = float(input("Zadaj teplotu: "))
jednotky = input("Vyber či je teplota v Celziach alebo Fahrenhaitoch (C/F): ")

if jednotky == "C":
    teplota = round((teplota * 9) / 5 + 32,2)
    print(f"Teplota vo F je: {teplota}°F")
elif jednotky == "F":
    teplota = round((teplota - 32) * (5 / 9),2)
    print(f"Teplota v Celziach je: {teplota}°C")

