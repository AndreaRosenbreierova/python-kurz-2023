# ------------------------------- TASK 01 -----------------------------------
# Načti od uživatele matematický operátor a 2 čísla a vypiš výsledek výpočtu.
# Program bude podporovat operátory +, -, / a *.
'''
Zadej operátor: +
Zadej první číslo: 3
Zadej druhé číslo: 9
Výsledek příkladu 3 + 9 je 12.
'''

#operator = input("Zadej operator:")
#prvni_cislo = int(input("Zadej cislo:"))
#druhe_cislo = int(input("Zadej cislo:"))






# ------------------------------- TASK 02 -----------------------------------
# Proměnná medal_table tentokrát obsahuje zisky jednotlivých druhů medailí států
# na olympiádě 2020.
medal_table = {
    "Cuba": { "gold": 7, "silver": 3, "bronze": 5 },
    "Spain": { "gold": 3, "silver": 8, "bronze": 6 },
    "Uganda": { "gold": 2, "silver": 1, "bronze": 1 },
    "Bahamas": { "gold": 2, "silver": 0, "bronze": 0 },
    "Ukraine": { "gold": 1, "silver": 6, "bronze": 12 },
    "San Marino": { "gold": 0, "silver": 1, "bronze": 2 },
}

# Vypiš název státu, který získal nejvíc bronzových medailí.


bronze_medals_slovnik = {}
for stat in medal_table:
    bronze_medals_slovnik[stat] = medal_table[stat]["bronze"]


max_pocet = 0
max_stat = ""
for stat in bronze_medals_slovnik:
    if bronze_medals_slovnik[stat] > max_pocet:
        max_pocet = bronze_medals_slovnik[stat]
        max_stat = stat
print(max_stat, max_pocet)

# ------------------------------- TASK 03 -----------------------------------
# V seznamu people máme seznam lidí s jejich daty narození. Vypište jména lidí,
# kteří se narodili v sudý rok.
people = [
    ["Jeong-Hui Mun", "09/12/1984"],
    ["Cezário Torres", "31/08/1993"],
    ["Josefina Löwe", "03/11/1982"],
    ["Gavrilo Milojević", "28/03/2002"],
    ["Liidia Tamm", "10/07/1963"],
    ["Matxin Zubizarreta", "19/02/1956"],
    ["Mykhail Klymenko", "01/10/1988"],
    ["Bibek Joshi", "05/03/2007"],
    ["Jan Vlk", "26/09/1995"],
    ["Xuân Hoàng", "29/08/1974"]
]

# ------------------------------- TASK 04 -----------------------------------
# Načti od uživatele celé číslo, zjisti, zda je dělitelné 8 a informuj
# o tom uživatele.
