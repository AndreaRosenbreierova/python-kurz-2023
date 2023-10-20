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
ranni_teploty = []
nocni_teplota = []
poledniAnocni_teploty = []


for teplota in teploty:
    prumerne_teploty.append(sum(teplota)/len(teplota))
    ranni_teploty.append(teplota[0])
    nocni_teplota.append(teplota[3])
    poledniAnocni_teploty.append([teplota[1],teplota[3]])

    
print(prumerne_teploty)
print(ranni_teploty)
print(nocni_teplota)
print(poledniAnocni_teploty)

#nepovinný úkol
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

prumerne_teploty = {teplota[0]:sum(teplota[1:])/len(teplota[1:]) for teplota in teploty}
print(prumerne_teploty)