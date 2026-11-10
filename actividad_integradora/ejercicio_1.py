
print("FACTURA DE COMPRA")
cliente = input("Nombre del cliente: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad comprada: "))

subtotal = precio * cantidad

if subtotal >= 200000:
    descuento = subtotal * 0.10
else:
    descuento = 0

total = subtotal - descuento

print("Cliente:", cliente)
print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total a pagar:", total)
