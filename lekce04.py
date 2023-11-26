""""
def hello_world():
    print("Hello world")

def hello_user(name):
    print("Hello, " + name)

def get_name():
    name = input("Name:")
    print("Ahoj uživaeli: " + name) 
    return name

def pizzeria(nazev, ananas = True):
    return f"Objednal sis pizzu{nazev}, obsahuje ananas: {ananas}"
def zpracuj_prihlasku(jmeno, gender=""):
    return f"{jmeno}, {gender}"

def znamky(seznam):
    novy_seznam = []
    
    for znamka in seznam:
       if znamka == 1:
            novy_seznam.append("vyborny")
       elif znamka == 2:
           novy_seznam.append("chvalitebny")
       elif znamka == 3:
           novy_seznam.append("dobry")
       elif znamka == 4:
           novy_seznam.append("dostatecny")
       elif znamka == 5:
           novy_seznam.append("nedostatecny")
       else:
           novy_seznam.append("ERROR")
     
    return novy_seznam

hodnoceni = [1, 2, 3, 4, 5]
print(znamky(hodnoceni))
print(znamky([1,4,5,6]))
print(pizzeria("Hawai", False))
print(pizzeria("Salami"))


hello_user(input("Name: "))
get_name()

jmeno = input("Zadej jmeno ")
gender = input("Zadej gender ")

if gender == "":
    print(zpracuj_prihlasku(jmeno))
else:
    print(zpracuj_prihlasku(jmeno, gender))
"""


def mult(cislo, cislo2):
    return (cislo * cislo2)
print(mult(2,5))    

def kilometry_na_mile(kilometry):
    return (kilometry * 0.62)
    
def mily_na_kilometry(mile):
    return(mile/0.62)

print(kilometry_na_mile(10))
print(mily_na_kilometry(60))

def hvezdicky(text, znak):
    return znak + text + znak 

text = input ("Zadej text: ")
print(hvezdicky(text, "*"))
    
    
