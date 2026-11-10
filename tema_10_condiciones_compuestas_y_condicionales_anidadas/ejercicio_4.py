print("***beca de estudio***")
promedio = float(input("Promedio académico: "))
matricula = input("¿Tiene matrícula activa? (si/no): ").lower() == "si"
if promedio >= 4.5 and matricula:
    print("Cumple los requisitos preliminares para la beca")
else:
    print("No cumple los requisitos preliminares")
