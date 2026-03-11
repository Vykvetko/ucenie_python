## Newtonova metoda 
# matematický algoritmus, ktorý postupne opravuje počiatočný odhad
# na zaklade chyby (rozdiel medzi g³ a x) vypočíta lepší odhad, až kým sa nepriblíži k správnemu výsledku.

x = int(input('Akému čislu treba vyrátať KOREŇ tretej odmocniny:  '))
odhad = float(input('Aký je náš odhad (aká bude tretia odmocnica) ')) 
print('Tretia mocnina našho odhadu = ', odhad**3)
dalsi_odhad = odhad - ((odhad**3 - x)/(3*odhad**2))
print('Dalši odhad = ', dalsi_odhad)