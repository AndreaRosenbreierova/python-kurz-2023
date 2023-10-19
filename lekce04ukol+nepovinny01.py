
def zadej_cislo():
    cislo = input("Zadejte číslo: ")
    cislo = cislo.replace(" ","")
    return cislo

def format_cisla(cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13:
        if cislo[:4] == "+420":
            return True
        else:
            return False
    else: 
        return False

zadane_cislo = zadej_cislo()
spravny_format = format_cisla(zadane_cislo)
print(spravny_format)

def zadej_zpravu():
    zprava = input("Zadej zprávu: ")
    return zprava

def format_zpravy(zprava):
    delka = len(zprava)  
    cena = int (delka / 180) 
    if delka != cena * 180:
        cena += 1
    cena = cena * 3    
    return cena
    
if spravny_format:
    zadana_zprava = zadej_zpravu()
    cena_zpravy = format_zpravy(zadana_zprava)
    print(cena_zpravy)


    