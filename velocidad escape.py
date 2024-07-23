# Importar la librería math
import math

# Solicitar los datos al usuario
r = float(input("Ingrese el radio en Kilometros:\n>"))  # 6371
g = float(input("Ingrese la constante g:\n>"))  # 9.8

# Calcular Velocidad escape
Velocidad = math.sqrt(2 * g * r * 1000)  # Convertir km a metros multiplicando por 1000

# Mostrar el resultado
print(f"La velocidad de escape es: {Velocidad:.1f} m/s")  # 11174.6
