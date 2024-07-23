#rentabilidad

# Solicitar los datos al usuario
P = float(input("Ingrese el precio de suscripcion:\n>"))  
Un = float(input("Ingrese el numero de usuarios normales:\n>"))
GT = float(input("Ingrese los gastos totales:\n>"))
Utianterior = float(input("Ingrese las Utilidades del año anterior:\n>"))

# Calcular utilidad
Utilidades = float(((P * Un) - GT))
razon = float(Utilidades / Utianterior)

# Mostrar el resultado
print(f"La razon entre las utilidades del año actual y el anterior es: {razon:.2f}")
