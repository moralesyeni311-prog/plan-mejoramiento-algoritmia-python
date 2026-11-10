print("VALIDACION DE REQUISITOS")

inscrita = input("¿Está inscrita? (si/no): ").lower() == "si"

identificacion = input("¿Presentó identificación? (si/no): ").lower() == "si"

if inscrita and identificacion:
    print("Cumple ambos requisitos")
else:
    print("No cumple  requisitos")