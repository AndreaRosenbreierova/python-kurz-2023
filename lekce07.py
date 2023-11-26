class Zamestnanec:
    def __init__(self, jmeno, pozice, pocet_dni, plat, firma = "Czechitas"):
        self.prac_pozice = pozice
        self.jmeno = jmeno
        self.pocet_dni = pocet_dni
        self.plat = plat
        self.firma = firma
    

    def vyuzij_dovolenou(self, dny):
        if dny > self.pocet_dni:
            return f"Na toto nemas narok, zbyva ti {self.pocet_dni} dni"
        else:
            self.pocet_dni = self.pocet_dni - dny
            return f"Na dovolenou mas narok, zbyva ti {self.pocet_dni}"
    
    def __str__(self):
        return f"Zamestnanec {self.jmeno}, pozice {self.prac_pozice}, dovolena: {self.pocet_dni}, firma: {self.firma}"

class Manager(Zamestnanec):
    def __init__(self, jmeno, pozice, pocet_dni, plat, pocet_podr, firma = "Czechitas"):
        super().__init__(jmeno, pozice, pocet_dni, plat, firma = "Czechitas")
        self.pocet_podr = pocet_podr

    def __str__(self):
        return super().__str__() + f"pocet podrizenych: {self.pocet_podr}"

Klara = Zamestnanec("Klara", "IT support", 25, 60000)
Matej = Zamestnanec("Matej", "Lektor", 20, 30000, "Gopas")
Jana = Manager ("Jana", "IT Manager", 30, 70000, 5)

print(Klara.vyuzij_dovolenou(10))
print(Matej.vyuzij_dovolenou(10))
print(Jana)
print(Jana.vyuzij_dovolenou(15))

#Nyní je naším cílem práce pro společnost, která se zabývá prodejem jízdenek a letenek.

# Vytvoř třídu Ticket, která bude mít atributy basic_price (základní cena) a seat_number (číslo sededla). Tato třída bude sloužit například pro cesty autobusem.
#Při cestování vlakem musíme řešit, jestli cestující využívá 1. nebo 2. třídu. Vytvoř třídu TrainTicket, která bude mít navíc atribut fare_class (uvažujeme možnosti economy a business). Dále naprogramuj metodu get_price(),
# která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, a cenu o 20 % vyšší oproti basic_price, pokud fare_class je business.
#U letenek řešíme třídu, kterou cestující letí, navíc ale musíme řešit i počet odbavených zavazadel. Vytvoř třídu PlaneTicket, která bude dědit od třídy TrainTicket a bude mít navíc atribut checkout_luggages, 
# který udává počet odbavených zavazadel. Naprogramuj metodu get_price(), která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, a cenu o 50 % vyšší oproti basic_price, 
# pokud fare_class je business. Dále připočti 2000 za každé odbavené zavazadlo (bez ohledu na třídu).
#Vytvoř jízdenku na vlak se základní cenou 150 do tříd economy i business. Zkontroluj, jakou hodnotu vrací metoda get_price().
#Vytvoř letenku se základní cenou 6000 do tříd economy i business s jedním odbaveným zavazadlem. Zkontroluj, jakou hodnotu vrací metoda get_price().

class Ticket: 
    def __init__ (self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number ,fare_class):
        super().__init__(self, basic_price, seat_number)
        self.fare_class = fare_class
    
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price
        elif self.fare_class == "business":
            return 1.2 * self.basic_price
        else:
            print("Neplatny fare_class")
    
        
    
    
    class PlaneTicket (TrainTicket):
      def __init__(self, basic_price, seat_number ,fare_class, checkout_luggage):
          super().__init__(basic_price, seat_number, fare_class)
          self.checkout_luggage = checkout_luggage
    
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price
        else:
            return 0.5 * self.basic_price
    

#Train = TrainTicket (250, fare_class: "1. trida")
#Plane = PlaneTicket (6000, checkout_luggage: 1)



          
    
    
    
    
    


