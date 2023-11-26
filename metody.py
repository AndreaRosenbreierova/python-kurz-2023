inzerat = "Povinne znalosti jsou Python, Java"
if "Python" in inzerat:
    print("Je to pro mě")
email = "a.rosen.gmail.com"
if "@" not in inzerat:
    print("Spatny email")
    
pohyby = [1200, -250, -800, 540, 721, -613, -222]
#print(pohyby[2])
#print(pohyby[2:])
print(min(pohyby))
print(max(pohyby))
print(sum(pohyby))

s = [2,3,4,5,6,7,8,9,10]
prumer = sum(s) / len(s)
print(prumer)
rozpeti = max(s) / min(s) 
print(rozpeti)

print('po ut st čt pá'.split(' '))
print('+'.join(['1', '2', '3', '4']))
print('/'.join(['dokumenty', 'dapraha', 'python', 'priklady']))

text = "Lekci vede lektor Martin"
novy_text = text.replace ("Martin","Marta")
print(novy_text)