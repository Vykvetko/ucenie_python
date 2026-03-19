x = float(input("Vyber si čislo pre x: "))
y = float(input("Vyber si čislo pre y: "))
if x == y:
    print("x a y su rovnaké")
if y != 0:
    print(f'Preto, x/y je {x/y}')
elif x < y:
    print("x je menšie ako y")
else:
    print("y je menšie ako x")
print("ĎAKUJEME!")

# odpoved = input("Aké je tvoje meno: ")

# if odpoved == "":
#     print("Nezadal si žiadne meno")
# else:
#     print(f"Vitaj v system {odpoved}")
