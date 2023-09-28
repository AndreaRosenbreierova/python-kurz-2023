sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = (input("Zadejte kod soucastky: "))


if kod in sklad:
    print ("Zbozi je skladem")
    mnozstvi = int (input("Zadejte mnozstvi: ")) 
    if sklad[kod] >= mnozstvi:
        print("Poptavku lze uspokojit v plne vysi")
        sklad[kod] -= mnozstvi
        print(sklad)
        if sklad[kod] == 0:
            sklad.pop(kod)
            print(sklad)        
    else: 
        print ("Soucastky lze prodat pouze omezene mnozstvi")    
        sklad.pop(kod)
        print(sklad)
else: 
    print ("Soucastka neni skladem")
 

