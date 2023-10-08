import json

body = {}
with open("body.json", mode="r",encoding="utf-8") as soubor:
    body = json.load(soubor)
#print(body)

vysledky = {}

for zaci in body:
  if body[zaci] >= 60:
      vysledky[zaci] = "Pass"
  else:
      vysledky[zaci] = "Fail"
#print(vysledky)

with open ("prospech.json", mode="w", encoding="utf-8") as soubor:
    json.dump (vysledky,soubor, ensure_ascii=False)
    
bonusy = {}
with open("bonusy.json", mode = "r", encoding="utf-8") as soubor:
    bonusy=json.load(soubor)
for zaci in bonusy:
    body[zaci] += bonusy[zaci]
print(body)

znamkovani = {}

for zaci in body:
    if body[zaci] >= 90:
        znamkovani[zaci] = 1
    elif body[zaci] >= 70:
        znamkovani[zaci] = 2
    elif body[zaci] >= 50:
        znamkovani[zaci] = 3
    elif body[zaci] >= 30:
        znamkovani[zaci] = 4
    else: 
        body[zaci] <= 29
        znamkovani[zaci] = 5
print(znamkovani)    

with open ("znamky.json", mode = "w", encoding="utf-8") as soubor:
    json.dump (znamkovani, soubor,ensure_ascii=False)