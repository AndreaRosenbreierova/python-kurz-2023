jmeno = "Andrea"
domena = "czechitas.cz"
email = jmeno + "@" + domena
print(email)


jmeno_a_prijmeni = input("Zadejte jmeno:")
print(jmeno_a_prijmeni.upper())

print(jmeno_a_prijmeni.lower())

jmeno = input("Zadejte jmeno:")
prijmeni = input("Zadejte prijmeni:")
print(jmeno[:1] + "." + prijmeni[:1]+ ".")

jmeno_a_prijmeni = jmeno[:1].upper() + jmeno[1:].lower() + " " + prijmeni[:1].upper() + prijmeni[1:].lower()
print(jmeno_a_prijmeni)

jmeno = input("Zadejte jmeno:")
prijmeni = input("Zadejte prijmeni:")
if len(jmeno) >=5:
    print(jmeno[:1] + " " + prijmeni) 
else:
    print(jmeno+ " " + prijmeni)