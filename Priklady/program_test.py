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

