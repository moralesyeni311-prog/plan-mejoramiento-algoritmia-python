print("***requisitos de inscripcion***")
edad = int(input("Edad: "))
documento = input("¿Tiene documento vigente? (si/no): ").lower() == "si"
cumple = edad >= 18 and documento
print("¿Cumple los requisitos?:", cumple)

