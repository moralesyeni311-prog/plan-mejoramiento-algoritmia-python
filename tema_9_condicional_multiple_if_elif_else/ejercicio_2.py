print("***clasificacion de temperatura***")
temperatura = float(input("Ingrese la temperatura: "))
if temperatura < 15:
    print("Fría")
elif temperatura <= 25:
    print("Templada")
else:
    print("Caliente")
