
class Auto:
    def __init__ (self,registracni_znacka, typ_vozidla, najete_km, dostupne: True, stav_tachometru, pocet_dni):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
        self.stav_tachometru = stav_tachometru
        self.pocet_dni = pocet_dni

    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            print("Potvrzuji zapujceni vozdila")
    
        else: 
            print("Vozidlo neni k dispozici")

    def get_info(self):
        return f"Registracni znacka vozidla je {self.registracni_znacka} a typ vozidla je {self.typ_vozidla}."

    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.stav_tachometru = stav_tachometru
        self.pocet_dni = pocet_dni
        self.dostupne = True
        cena = 0
        if pocet_dni <= 6:
           cena = pocet_dni * 400
        else:
            cena = pocet_dni * 300
        return f"Cena za pujceni auta je {cena} kc"    
        
    
    
Peuget = Auto ("4A2 3020", "Peugeot 403 Cabrio", 47534, True, 100000, 7)
Skoda = Auto ("1P3 4747", "Škoda Octavia", 41253, True, 100000, 10)


for i in range(4):
    vozidlo = input("Jake auto si chcete pujcit: ") 
    if vozidlo == "Peuget":
        print(Peuget.get_info())
        Peuget.pujc_auto()
    else:
        print(Skoda.get_info())
        Skoda.pujc_auto()

print(Peuget.vrat_auto(1000,5))


