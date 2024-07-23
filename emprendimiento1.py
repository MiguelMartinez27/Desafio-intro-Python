#rentabilidad

# Importar la librería math
import math

# Solicitar los datos al usuario
P = float(input("Ingrese el precio de suscripcion:\n>"))  
U = float(input("Ingrese el numero de usuarios:\n>"))
GT = float(input("Ingrese los gastos totales:\n>"))

# Calcular Velocidad escape
Utilidades = float((P * U) - GT)
Utilidades = math.ceil(Utilidades)

# Mostrar el resultado
print(f"La Utilidad es: {Utilidades}")  
