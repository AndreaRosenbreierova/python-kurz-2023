def vyuzij_dovolenou(zamestnanec, pocet_dni):
    if pocet_dni > zamestnanec["dovolena"]:
        print("Na toto nemas narok")
    else:
        print("Pozadavek schvalen")
        zamestnanec["dovolena"] = zamestnanec["dovolena"] - pocet_dni

znamestnanec4 = {
    "jmeno": "Alena Kucerova",
    "pozice": "IT Support",
    "dovolena": 25,
}

znamestnanec5 = {
    "jmeno": "Klara Kucerova",
    "pozice": "Senior IT Support",
    "dovolena": 25,
}

print(znamestnanec4["dovolena"])

vyuzij_dovolenou(znamestnanec4, 10)
vyuzij_dovolenou(znamestnanec5, 20)

print(znamestnanec4["dovolena"])
print(znamestnanec5["dovolena"])

def vyuzij_dovolenou(zamestnanec, pocet_dni):
        if pocet_dni > zamestnanec["dovolena"]:
            print("Na toto nemas narok")
        else:
            print("Pozadavek schvalen")
            zamestnanec["dovolena"] = zamestnanec["dovolena"] - pocet_dni

class Zamestnanec:
    def __init__(self, jmeno, pozice, pocet_dni, plat, firma = "Czechitas"):
        self.prac_pozice = pozice
        self.jmeno = jmeno
        self.pocet_dni = pocet_dni
        self.plat = plat
        self.firma = firma

    def ziskej_informace(self):
        return f"Zamestnanec {self.jmeno}, pozice {self.prac_pozice}, {self.pocet_dni}"
        

Klara = Zamestnanec("Klara", "IT support", 25, 60000)
Matej = Zamestnanec("Matej", "Lektor", 20, 30000, "Gopas")

print(Klara.ziskej_informace())
print(Matej.ziskej_informace())


# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.
# Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
# Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
# # Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.

class Package:
    def __init__(self, address, weight, state = "doručen"):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}"

Balik1 = Package("Jeremiasova", 5.5)
Balik2 = Package("Fintajslova", 6.0, "nedoručen")

print(Balik1.get_info())

print(Balik2.get_info())

#Vrať se k návrhu software pro zásilkovou společnost.

#U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print().
#Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení. Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen". Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".
#Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        else:
            self.state = "doručen"
            return "Doručení uloženo"


package1 = Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
package2 = Package("Jiřího z Poděbrad 9, Brno", 1.5, "doručen")

print(package1)
print(package2)

print(package1.deliver())
print(package1)  # Balík by měl být nyní ve stavu "doručen"
print(package1.deliver())  # Metoda by nyní měla vrátit zprávu, že balík již byl doručen

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        
        super().__init__(address, weight, state) 
        self.value = value
        
    def __str__(self):
        return super().__str__() + f"Cena je {self.value}"

valuable_package = ValuablePackage(address = "BBB", weight = 0.25, state = "na ceste", value = 1000)
print(valuable_package)
print(valuable_package.deliver())
    
    
