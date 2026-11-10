print("***tarifa de trasnporte***")

edad = int(input("Ingrese la edad: "))
if edad < 12:
    print("Tarifa infantil")
elif edad < 18:
    print("Tarifa juvenil")
else:
    print("Tarifa general")
