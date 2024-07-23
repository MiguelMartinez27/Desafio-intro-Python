#rentabilidad

# Importar la librería math
import math

# Solicitar los datos al usuario
P = float(input("Ingrese el precio de suscripcion:\n>"))  
Un = float(input("Ingrese el numero de usuarios normales:\n>"))
GT = float(input("Ingrese los gastos totales:\n>"))
Uanterior = float(input("Ingrese las Utilidades del año anterior:\n>"))

# Calcular utilidad
Utilidades = float((P * Un) + (1.5 * Up * P) - GT)
Utilidades = math.ceil(Utilidades)

# Mostrar el resultado
print(f"La Utilidad es: {Utilidades}")  
