
## ZÁPIS objektového typu 'string'
# string - používame na uloženie TEXTOVÉHO reťazca (použitie pismen, čisiel, znakov...)
# " " / ' ' - obidve uvodzovky majú rovnaký význam pri ZÁPISE
a = 'me'
b = "myself"
c = a + b # spojenie stringov 
d = a + " " + b # spojenie stringov s medzerou medzi nimi
opakovanie_vyrazu = b * 3 # zopakuje požadovaný string 3-krat

# funkcia len() - vráti počet znakov v požadovanom reťazci
len('auto') # slovo auto má 4 znaky => VYSLEDOK funkcie bude 4

s = 'abc'
len(s) # premenna s má 3 znaky => VYSLEDOK funkcie bude 3

dlzka_retazca = len(s) # uloženie POČTU znakov reťazca do premmenej
dlzka_retazca

# Priklady
b = ":"
c = ")"
s1 = b + 2*c
s1  # zobrazí nám smajlík :))

f = "a"
g = " b"
h = "3"
s2 = (f+g)*int(h)
print(s2) # zobrazí nam 3x ZASEBOU 'a b' => a ba ba b

## INDEXOVANIE - môžeme VYBRAŤ jednotlivý znak na určite pozicii vo VYRAZE
# indexy začínajú od 0 
s = "abc"
s[0] # vybere znak na UPLNE prvej pozicii vo výraze => a
s[1] # vybere znak na druhej pozicii => b
s[2] # vybere znak => c
s[3] # toto nám hodi error => keďže to chce vybrať 4. znak ale náš vyraz ma len 3 znaky
s[-1] # -1 => vyberie nám POSLEDNY znak z výrazu (PRVÝ znak od konca) => c
s[-2] # -2 => b
s[-3] # -3 => a

## SLICING -  vyrezanie časti reťazca (vyber časti podľa rozsahu indexu) 
# [start : end : step]
# start — od ktorého indexu VYBERÁME čast 
# end — po ktorý index (tento INDEX sa nezapočítava => VYBERÁ end - 1)
# step — o koľko pozícií sa posúvame 

s = "abcdefgh"
s[3:6] # vyberie znaky od indexu 3 po index 5 => def
s[3:6:2] # vyberie znaky od indexu 3 po index 5, ale každé druhé pismeno => df
s[:] # vypíše nám CELY výraz => abcdefgh => vytvorí KOPIU toho výrazu (vytvorí nový objekt v pamäti)
s[::-1] # keďze je step -1 => vypíše nam celý VYRAZ odzadu 
s[4:1:-2] # vyberie znaky od indexu po 4 po index 2 a keďže je step -2 => ec

## UPRAVA / MANIPULACIA s objektami
# objekty typu STRING su nemenné - nemôžeme ich upraviť
# ale môžeme vytvoriť NOVE objekty, ktoré budu ROVNAKE / INÉ verzie pôvodneho objektu
# PREMENNA môže byť priradená len k JEDNOMU objektu !
s = "car"
s[0] = 'b'  # TOTO nám hodí error => keďže nemôžeme upravovať existujuci OBJEKT

s = 'b'+s[1:len(s)]  # TOTO bude fungovať => keďže premennej s priradíme uplne novú hodnotu => VZNIKNE NÁM NOVÝ OBJEKT

## ZOBRAZOVANIE / VYPISOVANIE 
# pri písaní kodu tu v súbore => musíme mu zadať prikaz PRINT na vypísanie
a = "the"
b = 3
c = "musketeers"
print(a, b, c) # vypíše nám VŠETKÝ požadované premenne zasebou v jednom riadku
print(a + b + c) # toto nám hodí chybu keďže dokáže spajať len STRINGOVÉ typy (textové), b => je INT (čiselny typ objektu)
print(a + str(b) + c) # funguje, keďže sme pre premmennu b zmenili typ z INT na STRING

cislo = 5
print("Moje cislo je", cislo)
s = "Moje cislo je " + cislo # hodí nám chybu => keďze sa text snažím spojiť s objektom typu INT
s = "Moje cislo je " + str(cislo) # spravne => museli sme zmeniť typ premmenej cislo na STRING => Môžeme spojiť s textom!
print(s)

x = 1
x_str = str(x)
print("Moje oblubene cislo je", x, ".", "x =", x) # funguje správne => keďže to NESPAJAME, ale vypisujeme hodnotu premennej x 
print("Moje oblubene cislo je " + x_str + ". " + "x = " + x_str) # funguje správne => keďže spájanie funguje len so STRINGOVYMI objektami

## Uživatelske vstupy (hodnoty, ktoré zadávame my)
# input(Text: ) - zobrazi to čo sme ZADALI do zatvoriek a čaká čo UŽIVATEL zadá
#               - vždycky hodnotu čo zadáme berie ako STRING! => keď chceme uložiť hodnotu ako čislo INT, musíme použiť cast

# Priklad 1:
text = input("Napíš niečo: ") # následne to čo UŽIVATEL zadá, priradí premmenej text
print(5*text)

# Priklad 2:
cislo1 = input("Napis cislo: ")
print(5*cislo1) # zobrazí nám 5krát zasebou číslo, ktore sme zadali => keďže 'input' priraduje hodnotu ako STRING

cislo2 = int(input("Napís cislo: "))
print(5*cislo2) # zobrazí nám číslo ktoré sme zadali a vynásobi ho 5 => keďže sme hodnotu z 'input' konvertovali na typ INT, takže to bere ako ČISLO

# Príklad 3:
# Newtonova metoda - algoritmus na vypočitanie približnej hodnoty koreňov
# Kubická odmocnina z čísla x je také číslo, ktoré keď vynásobíš samo sebou 3-krát, dostaneš x.
x = int(input('Akému čislu treba vyrátať koren tretej odmocniny:  '))
odhad = int(input('Aký je náš odhad (aká bude tretia odmocnica) ')) # Je to prvé číslo, od ktorého algoritmus začne hľadať riešenie. Newtonova metóda tento odhad postupne opravuje a každým krokom sa približuje k správnej hodnote.

print('Tretia mocnina našho odhadu = ', odhad**3)
dalsi_odhad = odhad - ((odhad**3 - x)/(3*odhad**2))
print('Dalši odhad = ', dalsi_odhad)


## F-STRINGS 
# jednoduchšie zapisanie zapísania textu spoločne s premennými / vyrazmi 
# vyrazy a premenne možeme použiť priamo v texte, a to čo chceme doplniť z PREMENNYCH ALEBO VYRAZMI označíme {} zatvorkami spolu s textom
# print(f"text {premenna/vyraz} text")
cislo = 4000
zlomok = 1/3
print(cislo*zlomok, 'je', zlomok*100, '% z', cislo) # prvé riesenie - za zlomok*100, => , spraví medzeru navyše
print(cislo*zlomok, 'je', str(zlomok*100) + '% z', cislo) # druhe riešenie - vyrieši 1. problem
print(f'{cislo*zlomok} je {zlomok*100}% z {cislo}') # najlepsie riešenie - najnovšie, najviac prehladné

# Priklady (pomocou f-strings)
# Vypočíta kolko je 1/3 (33.3%) z požadovaného ČISLA
tretina = 1/3
moje_cislo = int(input("Vlozime cislo, ktorého 1/3 chceme zobraziť: "))
print(f"{tretina*moje_cislo:.2f} je {tretina*100:.2f}% z {moje_cislo}")

## BOOLEAN (typ)

volny_cas = 15
spaci_cas = 8
print(spaci_cas > volny_cas) # keďze "spaci_cas" je menší ako "volny_cas" => výraz v zatvorke je FALSE + ho zobrazí

test1 = True
test2 = False 
obidve = test1 and test2 
print(obidve) # keďže test1 je "true" a test2 "false" a do PREMENNEJ "obidve" sme uložili tieto premenne s operatorom and => musia byť obidve TRUE, aby nám printlo TRUE

## Vetvenie (podmienky - if/else) 
# Priklad 1
volny_cas = 14
spaci_cas = 8
if (volny_cas + spaci_cas) > 24:
    print("Nemožné.")
elif (volny_cas + spaci_cas) == 24:
    print("Plný rozvrh")
else:
    zostatok_casu = abs(24-volny_cas-spaci_cas)
    print(zostatok_casu,"hodín volného času nám ostalo")
print("Koniec dna")

# Chybne zadanie + oprava!
x = int(input("Vloz cislo x: "))
y = int(input("Vloz rozdielne cislo pre y: "))
if x == y:
    print(x,"je rovnake ako",y)
print("Tieto su rovnaké!") # zly zápis -> keďže tuto vetu vypíše vždy, nezaleží na tom či je splnená podmienka ako nie
    print("Tieto su rovnaké!") # dobry zapís => keďže tuto vetu chceme vypísať len keď je splnená podmienka, takže musíme tomu prispôbiť aj ODDELENIE



# NESTED BRANCHING (vnorené vetvenie)
# Priklad 1:
x = float(input("Vyber si čislo pre x:"))
y = float(input("Vyber si čislo pre y:"))
if x == y:
    print("x a y su rovnaké")
    if y != 0:
         print(f'Preto, x/y je {x/y}')
elif x < y:
    print("x je menšie ako y")
else:
    print("y je menšie ako x")
print("ĎAKUJEME!")


############## YOU TRY IT ###############
# What's printed when y = 2, y = 20, y = 11?
# What if "if x <= y:" becomes "elif x <= y:"

# answer = ''
# x = 11
# y = 2 # try 20 and 11
# if x == y:
#     answer = answer + 'M'
# if x <= y:   # try making this line: elif x <= y:
#     answer = answer + 'i'
# else:
#     answer = answer + 'T'
# print(answer)

#########################################






# Ake su hodnoty s1 a s2
s1 = "a" + "b"
s1 # zobrazí ab keďže do s1 sme uložili "a" + "b"

d = "hi"
e = " ana"
s2 = d + 2*e
s2 # zobrazí hi ana ana, keďže mame 2x ana s MEDZEROU na začiatku a predtým + hi


# Ake su "VYBRATE" časti premennej s
s = "ABC d3f ghi"
s[0:3:1] # zobrazí od indexu 0 teda od A po index 2 takže po C => 'ABC'
s[0:4] # zobrazi od indeu 0 teda od A po index 3 takže to je prazdne miesto => 'ABC '
s[8:len(s):3] # zobrazi od indexu 8 po index 10 a každý tretí znak takže => 'g'
s[2::-1] # zobrazi od indexu 2 po začiatok, keďže step máme -1 => 'CBA'


# Practice 3: What does this print?
# Note that a += b is the same as a = a + b
# answer = ''
# x = 11
# # try with y = 2 and y = 12
# y = 2
# if len(str(x)) == len(str(y)):
#     if y != 0 and x%2 == 1:
#         answer = answer + "x / y is " + str(x/y)
# elif x < y:
#     answer += "\nx is smaller"  # \n inserts a newline character in the string
# else:
#     answer += "\ny is smaller"
# print(answer)



# Practice 4: Uncomment the code below and:
# What does it print when a = 6 and b = "6"
# What does it print when a = "1" and b = 1
# What does it print when a = 3 and b = 3
# What does it print when a = "1" and b = "1"

# if ( a == int(b) ):
#     print("int conversion")
# if ( a == int(b) ) and ( str(a) == b ):
#     print("int and str conversion")
# else: 
#     print("interesting")
    
#########################################
############### END AT HOME ##########################
#########################################


#########################################
############### ANSWERS TO LECTURE ##########################
#########################################
# You Try It 1: Write a program that: 
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run

# your code here
# verb = input("Type in a verb: ")
# print("I can", verb, "better than you!")
# print((verb+" ")*4+verb)


# You Try It 2: Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints a bool depending on whether the guess matches the secret.

# your code here
# secret = 7
# guess = int(input("Guess a number between 0 and 10: "))
# print(secret == guess)


# You Try It 3: Buggy, fix it!
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x,"is the same as",y)
# print("These are equal!")

# Fixed:
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x,"and",y)
#     print("These are equal!")


# You Try It 4: Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints whether the guess is too low, too high, or the same as the secret. 

# your code here
# secret = 7
# guess = int(input("Guess a number between 0 and 10: "))
# if guess == secret:
#     print("You are correct.")
# elif guess < secret:
#     print("Your guess is too low.")
# else:
#     print("Your guess is too high.")

#########################################
############### END ANSWERS TO LECTURE ##########################
#########################################
