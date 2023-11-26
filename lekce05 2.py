
"""
import swapi

print(swapi.getPerson(3))

jmeno: str = "Michal"
vek: int = 26
hodnoceni: float = "Jsem string"
print(hodnoceni)

def znamka(pocet_bodu: list, bonus_body: dict = 20) -> int:
    if pocet_bodu > 90:
        return 1

print(znamka(91))

znamky = [0, 2, 3, 1, 1, 3]
pisemky = [
    
]
nove_znamky = []

for z in znamky:
    nove_znamky.append(z + 1)
    
    print(f"Stare namky: {znamky}")
    print(f"Nove znamky: {nove_znamky}")
    

def total_price(persons, breakfast=False):
    cena = 850*persons
    if breakfast:
        cena += 125*persons
    return cena
    
    print(total_price(3))
    print(total_price(2, True))"""



cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
    
print([2*cislo for cislo in cisla])

print([-1*cislo for cislo in cisla])

print([cislo**2 for cislo in cisla])

print([str(cislo) for cislo in cisla])

print([int(cislo) for cislo in cisla])

jmena = ["Roman", "Jan", "Miroslav", "Petr", "Gabriel"]

print([len(jmeno) for jmeno in jmena])

print([jmeno.upper() for jmeno in jmena])

print([jmeno+"a" for jmeno in jmena])

print([jmeno.lower()+"@email.cz" for jmeno in jmena])


def mean(seznam):
    return sum(seznam)/len(seznam)
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerne_teploty = []
for den in teploty:
    prumerne_teploty.append(sum(den)/len(den))
print(prumerne_teploty)

prumerne_teploty = [sum(den)/len(den) for den in teploty]
print(prumerne_teploty)

prumerne_teploty = [mean(den) for den in teploty]

print([den[0] for den in teploty])

print([den[-1] for den in teploty])

print([[den[1], den[-1]] for den in teploty])





    

    