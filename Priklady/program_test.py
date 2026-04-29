## SHIFT + ALT + V - PRIDANIE / ODOBRATIE komentu 
# Priradenie klavesy
# vo VS Code -> File -> Preferences -> Keybord Shorcuts -> Toggle Line Comment

# x = float(input("Vyber si čislo pre x: "))
# y = float(input("Vyber si čislo pre y: "))
# if x == y:
#     print("x a y su rovnaké")
# if y != 0:
#     print(f'Preto, x/y je {x/y}')
# elif x < y:
#     print("x je menšie ako y")
# else:
#     print("y je menšie ako x")
# print("ĎAKUJEME!")

# odpoved = input("Aké je tvoje meno: ")

# if odpoved == "":
#     print("Nezadal si žiadne meno")
# else:
#     print(f"Vitaj v system {odpoved}")

# odpoved = ''
# x = 11
# y = 20 # vyskušat 2,11,20
# if x == y:
#     odpoved = odpoved + 'M'
# if x <= y:   # elif x <= y:
#     odpoved = odpoved + 'i'
# else:
#     odpoved = odpoved + 'T'
# print(odpoved)

# ak máme x a y s rovnakými hodnotami a použijeme za prvým if -> if x <= y: - ZOBRAZÍ NAM Mi, keďze je splnena aj prvá aj druha if podmienka
#                                                             -> elif x <= y: - ZOBRAZI NAM len M, keďže prvá if podmienka je splnená, tak tuto dalsiu elif IGNORUJE

# odpoved = ''
# x = 11
# # vyskušat s Y = 2 a Y = 12
# y = 12
# if len(str(x)) == len(str(y)):
#     if y != 0 and x%2 == 1:
#         odpoved = odpoved + "x / y je " + str(x/y) # do premmenej odpoved nám vloží "x/y is ...." pretože odpoveď je 'prazdny string'
#     if x < y:
#         odpoved += "\nx is mensie"  
# elif x < y:
#         odpoved += "\nx je mensie"
# else:
#     odpoved += "\ny je mensie"
# print(odpoved)

# x = 12
# y = 13

# len(str(x))
# len(str(y))

# a = 2
# b = "2"
# print(f"Typ a: {type(a)}")
# print(f"Typ b: {type(b)}")
# if (a == int(b)):
#     print("INT konverzia") # ak sa hodnota 'a' rovná int hodnote 'b' => vypíše INT konverzia
# if (a == int(b)) and (str(a) == b): 
#     print("INT a STR konverzia") # ak je SPLNENÁ PRVÁ PODMIENKA + hodnota str 'a' sa rovná hodnote str 'b' => vypiše INT a STR konverzia
# else: 
#     print("Žiadna konverzia")

# smer = input("Si strateny v lese, kam chces isť VLAVO alebo VPRAVO: ")
# while smer == "VPRAVO":
#     smer = input("Si strateny v lese, kam chces isť VLAVO alebo VPRAVO: ")
# print("VYŠIEL SI Z LESA!")

# a = 10
# b = "10"
# if a == int(b):
#     print("A")
# if str(a) == b:
#     print("B")

# n = 0
# smer = input("Kam isť vlavo alebo vpravo: ")
# while smer == "vpravo":
#     n = n + 1
#     if n > 2:
#         print(":(")
#     smer = input("Kam isť vlavo alebo vpravo: ")
# print("Si vonku!")

# x = 4 # premenna, do ktorej uložime HODNOTU ktorej chceme vyrátať faktorial
# faktorial = 1
# i = 1 # premenna pre CYKLUS = funguje ako POČÍTADLO, kolkokrát sa má WHILE cyklus vykonať
#       # postupne ide od 1 po premennu 'x'
# while i <= x:
#     faktorial = faktorial * i
#     i = i + 1
# print(f"Faktorial čísla {x} je {faktorial}")

# n = 0
# while n < 5:
#     print(n)
#     n += 1

# x = 4 # premenna, do ktorej uložime HODNOTU ktorej chceme vyrátať faktorial
# faktorial = 1
# for i in range(1, x + 1, 1):
#     faktorial = faktorial * i
# print(f"Faktorial čisla {x} je {faktorial}")

# help(0)

# import tkinter
# import random

# canvas = tkinter.Canvas(bg='red', width=300, height=300)
# canvas.pack()

# for i in range(10):
#     x = random.randint(1, 300)
#     y = random.randint(1, 300)
#     farba = 'blue'
#     canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

# tkinter.mainloop()

# ab = """prvy riadok
# matko
# hmircik"""

# print(ab)

# x = int(input("Zadaj čislo: "))
# for i in range(1, x + 1, 1):
#     if i % 5 == 0:
#         print(i)

        
cislo = int(input("Zadaj cele čislo: "))
celkovo = 0
while True:
    r = cislo%10
    celkovo = celkovo + r
    cislo = cislo//10
    if cislo == 0:
        break
print(celkovo)
