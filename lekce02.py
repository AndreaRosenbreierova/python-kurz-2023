jmena = ["Martin", "Michal", "Milada", "Jana"]
#print(jmena[2])

knihy = ["Temna noc", 450, True, True]
knihy[0]= "Milosrdna vrazda"

knihy2 = {
    "Nazev":"Ananas na pizzu patri",
    "Cena": 0,
    "Skladem": True,
}
print(knihy2)
print(knihy2.keys())
print(knihy2.values())
print(knihy2["Nazev"])
knihy2["Cena"] = 100

print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")

knihy2["Autor"] = "Andrea Rosenbreierova"
print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}, autor: {knihy2['Autor']}")

if "Autor" in knihy2:
     print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}, autor: {knihy2['Autor']}")
else: 
    print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")
    

vysvedceni = {
    "Anglictina": 1,
    "Cestina": 2,
    "Matematika": 3
}
print(vysvedceni.keys())
print(vysvedceni.values())


sales = {
    "Zkus me chytit": 4156,
    "Vrah zavola v deset": 5681,
    "Zlocinny steh": 2565,
}

sales["Noc, ktera me zabila"] = 0
sales["Vrah zavola v deset"] = sales["Vrah zavola v deset"]  + 100
print(f"Zkus me chytit: {sales['Zkus me chytit']}, Vrah zavola v deset: {sales['Vrah zavola v deset']}, Zlocinny steh: {sales['Zlocinny steh']}, Noc, ktera me zabila: {sales['Noc, ktera me zabila']} " )

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
cislo = int (input("Zadejte číslo:"))
if cislo in tombola:
    tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",}
    print("vyhravas!")
else: 
    print("Bohuzel nevyhravas nic.")
    
 
    
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
jmeno = int (input("Zadejte jméno hosta:"))



