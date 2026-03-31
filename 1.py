## type(hodnota) - zistíme OBJEKTOVY typ POŽADOVANEJ hodnoty/vyrazu 
# Objekty v pamati maju svoje typy => typy nam určújú ake operácie môžeme s objektami robiť
type(5)
type(3.0)
type('auto')
type('-')

## Konvertujeme hodnotu v zatvorke do POŽADOVANÉHO objektového typu 
float(3)
int(3.9)
round(3.9)

## Zapis vyrazov 
3+2
 
type((4+2)*6-1)
float((4+2)*6-1)

## Zapisovanie premmených 
pi = 355/113


# vypočita približnu hodnotu pi
pi = 355/113
radius = 2.2
area = pi*(radius**2)
circumference = pi*(radius*2)

## ZAPISOVANIE KODOV (code style) ##

# Prvý zapis - ZLY ZAPIS, takto to nezapisovať
# spravi vypočty
a = 355/113 *(2.2**2)
c = 355/113 *(2.2*2)

# Druhý zapis - ZLY ZAPIS - komentuje presne co robi ten kod a premenne su pomenované JEDNYM znakom !
p = 355/113
r = 2.2
# vynasobi p s r na druhú
a = p*(r**2)
# vynasobi p s r 2-krat
c = p*(r*2)

# Tretí zápis - SPRÁVNY ZÁPIS
# Vypočita obsah a obvod kruznice za pouzitia
pi = 355/113
radius = 2.2
area = pi*(radius**2)
circumference = pi*(radius*2)


# ZMENA priradenia hodnoty pre premennu radius
pi = 3.14
radius = 2.2
area = pi*(radius**2)
radius = radius+1


## Vymena hodnot 
# Danému x a y, vymente hodnoty bez toho aby sme ich priamo PRIRADILI do premennej
x = 1			
y = 2
# ZLE RIEŠENIE - keďže Y bude ako x (1), tak aj X bude ako y (1)
# TO znamená že riešenie je zle, keďze y aj x = 1
y = x
x = y
# SPRÁVNE RIEŠENIE - vytvoríme 3 premennu
temp = y
y = x
x = temp


## KOMENTOVANIE KODU
# používame jednu # a všetko za tým na DANOM riadku Python ignoruje
# ## - dve mriežky, nemaju specialnu funkciu => používame pre lepšiu čitatelnosť kódu (NADPISY, OZNAČENIE NIAKYCH SEKCII...)

# Viac riadkový komentár
# p= 355/113i 
# radius = 2.2
# area = pi*(radius**2)
# circumference = pi*(radius*2)

# Vysvetlenie prikazu - # za prikazom
rychlost = 90  # km/h
cas = 60  # sekund


## Autodoplnovanie názvu DLHÝCH premenných (vo VS Code, iných editoroch...)
# Zadanie premenej
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# Ked ju chceme znova napísať, stači napisať a_ve a TAB.
# a_ve + TAB =>
a_very_long_variable_name_dont_name_them_this_long_pls

## Escape Characters (Specialne znaky)
# používame ich na zapísanie špecialnych znakov (medzery, uvodzovky v texte...) v STRINGOCH
# ZAPISUJEME ICH pomocou SPÄTNEHO LOMITKA ( / ) !!

# NOVY RIADOK v STRINGU
# použijeme \n pred TEXTOM (stringom), ktorý chceme ODDELIŤ na nový riadok
print("Ahoj,\nMoje meno je Martin\nSom zo Ziliny")

# ODSADENIE (odsek)
# použijeme \t pred TEXTOM, ktorý chceme "POSUNUŤ/ODSADIŤ"
print("Ahoj\tMatko")

# VYPISANIE UVODZOVIEK V TEXTE
# ak by sme použili len klasické "" v texte, bralo by sa to ako koniec stringu
# použijeme \" - PRED a ZA textom, ktorý chceme vložiť do úvodzoviek
print("Ahoj, moja prezyvka je \"Vykvet\"")

# VYPISANIE APOSTROFU V TEXTE
# rovnaký dôvod ako pri úvodzovkách
# použijeme \' - PRED a ZA textom, ktory chceme vložiť do apostrofou
print("Ahoj, moje priezvisko je \'Hmircik\'")

# ZOBRAZENIE SPÄTNEHO LOMÍTKA V TEXTE
# použijeme \\ 
print("Adresár: C:\\Martin\\Desktop")