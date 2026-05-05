#Pide precio de un producto y si el cliente es socio (s/n).
#Reglas de descuento:
#• Precio > 50.000 AND socio → 20% descuento
#• Precio > 50.000 AND no socio → 10% descuento
#• Precio <= 50.000 AND socio → 5% descuento
#• Resto → sin descuento
#Muestra precio final con 2 decimales.

print("========================================")

precio = float(input("Precio del producto: "))
socio = input("¿Eres socio? (s/n): ").lower()

if precio > 50000 and socio == "s":
    porcentaje = precio * 0.2
    precio = precio - porcentaje
    print(f"Precio final: {precio:.2f}")

elif precio > 50000 and socio == "n":
    porcentaje = precio * 0.1
    precio = precio - porcentaje
    print(f"Precio final: {precio:.2f}")

elif precio <= 50000 and socio == "s":
    porcentaje = precio * 0.05
    precio = precio - porcentaje
    print(f"Precio final: {precio:.2f}")

else:
    print(f"Precio final: {precio:.2f}")

print("========================================")