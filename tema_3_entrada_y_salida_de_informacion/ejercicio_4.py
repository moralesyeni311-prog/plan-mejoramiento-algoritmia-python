print("***factura de un pedido***")
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = precio * cantidad

print("------ FACTURA ------")
print("Producto:", producto)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Subtotal:", subtotal)