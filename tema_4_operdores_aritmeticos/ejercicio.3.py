elementos = int(input("Cantidad de elementos: "))
personas = int(input("Número de personas (mayor que cero): "))
por_persona = elementos // personas
sobran = elementos % personas
print("Elementos por persona:", por_persona)
print("Elementos sobrantes:", sobran)
