
seznam = [100, 200, 300, 400]
soucet = 0
for polozka in seznam:
    soucet += polozka #soucet = soucet + polozka
    
print(soucet)

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
for klic in sales: 
    print(sales[klic])
    
for klic, hodnota in sales.items():
    print(f"nazev:{klic}, pocet prodanych kusu: {hodnota}")

for value in sales.values():
    print(value)

pocet_prodanych_kusu = 0

for klic, hodnota in sales.items():
    pocet_prodanych_kusu += hodnota 
print(pocet_prodanych_kusu)

hodnoceni = ["Kniha 1", "Kniha 2", 5, "Kniha3", 3.3]
hodnoceni1 =[["Kniha1",4], ["Kniha2", 5], ["Kniha3", 3.3]]

print(hodnoceni1[0][1])
print(hodnoceni1[0][0][0])

for polozka in hodnoceni1:
    print(polozka[0])

for polozka in hodnoceni1:
    print(polozka[0] + " " + str(polozka[1]))

books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

print(books[2])
print(books[0])
print(books[2]["title"])
