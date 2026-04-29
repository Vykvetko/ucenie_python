## Použitie cyklusu WHILE - string (text)

# Priklad 1:
smer = input("Si strateny v lese, kam chces isť VLAVO alebo VPRAVO: ")
while smer == "VPRAVO":
    smer = input("Si strateny v lese, kam chces isť VLAVO alebo VPRAVO: ")
print("VYŠIEL SI Z LESA!") # keď napíšeme VLAVO => vykona sa tento príkaz, keďže je to oddelene ODSEKOM na úrovni while

# Priklad 1.1:
smer = input("Si strateny v lese\n****************\n****************\n:)\n****************\n****************\nKam chces ist vlavo alebo vpravo: ")
while smer.lower() == "vpravo": # funkcia smer.lower() - prekonvertuje OBSAH premmenej 'smer' na MALÉ písmená
   smer = input("Si stratený v lese\n****************\n******       ***\n  (╯°□°）╯\n     ︵ \n    ┻━┻\n****************\n****************\nKam chces ist vlavo alebo alebo vpravo: ")
print("\nDOSTAL SI SA VON Z LESA, HURÁ!\n\o/")

## Použitie cyklus WHILE - int (čisla)
n = int(input("Vlozte kladné cele číslo: "))
while n > 0:
    print("x")
    n = n-1 # ak je splnená podmienka že 'n' je väčšie ako 0, zobrazí "x" a s HODNOTY premennej 'n' odpočíta 1 => takže sa cyklus o JEDEN krat menej vykoná
            # ak by sme tento riadok nepoužili => NEKONEČNY CYKLUS
            # dá sa zapisať ako n -= 1

# Priklad nekonečného cyklu:
# CTRL + C - prerušenie
while True:
    print("Nieeee")


# Prerobiť kód, tak aby program ukázal smutný smajlík
# keď sa WHILE cyklus vykoná VIAC ako 2-krat => ZADAME 2-krat VPRAVO 
# Zadanie:
where = input("Go left or right? ")
while where == "right":
   where = input("Go left or right? ")
print("You got out!")

# Riešenie:
n = 0 
smer = input("Kam isť vlavo alebo vpravo: ")
while smer == "vpravo":
    n = n + 1 # keďže n sme definovali ako 0, každe PREBEHNUTIE cyklu zvyši hodnotu o 1 => funguje ako počitadlo vpodstate
    if n > 2:
        print(":(")
    smer = input("Kam isť vlavo alebo vpravo: ")
print("Si vonku!")

# Priklad 2 (Faktorial, while loop):

x = 4 # premenna, do ktorej uložime HODNOTU ktorej chceme vyrátať faktorial
faktorial = 1
i = 1 # premenna pre CYKLUS = funguje ako POČÍTADLO, kolkokrát sa má WHILE cyklus vykonať
      # postupne ide od 1 po hodnotu v 'x'
while i <= x:
    faktorial = faktorial * i
    i = i + 1
print(f"Faktorial čísla {x} je {faktorial}")

## Použitie cyklusu FOR
# Odporučené použitie keď VIEM KOLKOKRÁT sa má cyklus vykonať!
 
for n in range(5):
    print(n)

# Porovnanie s while:

n = 0
while n < 5:
    print(n)
    n += 1

## Priklad 2.1 (Faktorial, for loop):

x = int(input("Zadajte číslo, ktorého faktorial chcete vyrátať:")) # x = premenna, do ktorej uložime HODNOTU ktorej chceme vyrátať faktorial
faktorial = 1
for i in range(1, x + 1, 1):
    faktorial = faktorial * i
print(f"Faktorial čisla {x} je {faktorial}")


for i in range(1,4,1): # v každom cykle premenná i dostane ďalšiu hodnotu z ROZSAHU range(1, 4, 1)
    print(i) # tu vpodstate doplnenú hodnotu vypíše keďze => print(i)


for j in range(1,4,2): # po každom CYKLE nám doplní KAZĎU DRUHÚ hodnotu do premmenej! => keďže STEP je 2
    print(j*2) 

for me in range(4,0,-1): 
     print("$"*me)  # vypíše nam OPAČNÚ PYRAMIDU z $, ktorá bude ZAČINAŤ $$$$ a KONČIŤ $

# Príklad 3:

mysum = 0 # premenna, kde budeme ukladať PRIEBEŽNÚ SUMU sučtu hodnôt v SEKVENCÍI HODNOT (range(10))
for i in range(10):
   mysum += i # po každom CYKLE, pripočítam k 'mysum' hodnotu ktorá nasleduje z range(10) (0,1,2,3.... po 9)
print(mysum) # vypiše sučet všetkých čisel v ROZSAHU HODNOT (range(10))

# Príklad 3.1:

mysum = 0
for i in range(7, 10):
    mysum += i # k premmenej mysum (teda k 0) po každom cykle PRIČÍTAME hodnotu z rozsahu 7 po 9 => keďže range(10)
print(mysum) # mysum (0) + 7 => mysum (7) + 8 => mysum (15) + 9 = 24

# Príklad 3.2:
# Oprav kód, aby sme premennami (start, end) si určili 
# ROZSAH ČISEL, ktorých hodnotu chceme sčítať VRÁTANE HODNOT (start a end)
mysum = 0
start = 3
end = 5
for i in range(start, end + 1): # musíme ku end pridať '+ 1', aby sme mohli aj tuto hodnotu SČÍTAŤ 
    mysum += i
print(mysum)


## CVIČENIA 

# Test 1: 
# Zadefinuj premennu x, ktorá bude obsahovať kladne cele čislo -> int > 0.
# Vypišme všetky ČISLA ktoré su delitelne 5kou a nachádzaju sa v rozmedzi
# 1 po x - OBIDVE VRATANE! 
# 
# Napr. ak x = 15, tak zobrazí 5, 10, 15
# Napr. ak x = 14, tak zobrazí 5, 10

x = int(input("Zadaj čislo: "))
for i in range(1, x + 1, 1):
    if i % 5 == 0:
        print(i)




# Test 2:
# Zadefinuj premennu 'cislo', do ktorej uložíme KLADNE CELE číslo
# Vypíš sučet všetkých jej jednotlivých číslic 
# Napr. cislo = 1234, (1+2+3+4) => program vypíše 10
# Pomôcka: Jednotlivé čislice vieme dostať tým, že sa pozrieme na zvyšok 
# po delení premennej 'cislo' DESIATIMI!


cislo = int(input("Zadaj cele čislo: "))
celkovo = 0
while True:
    r = cislo%10 # to nám vždy "ODSEKNE" posledné ČISLO z hodnoty v premmenej 'cislo'   
                 # z 1234 % 10 => ZVYŠOK po delení je 4 (posledna čislica)
    celkovo = celkovo + r # tu sa pripočítame ten zvyšok po DELENI (4)
                          # čo je POSLEDNÁ čislica z požadovaného čisla
    cislo = cislo//10 # // - CELOČISELNE DELENIE! - použijeme aby sme mohli znovať "ODSEKNUŤ" posledné čislo
    if cislo == 0:
        break
print(celkovo)







