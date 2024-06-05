#Archivo: Ejercicio 1 semana 3
#Autora: Marce Alpízar
#Fecha: 3/6/2024
#Descripción: Para calcular el área deberá solicitar la base y altura del triángulo,el radio del círculo, el ancho y altura para los brazos, las piernas y el cuerpo.
import math

# Solicitar la base y altura del triángulo
base_triangulo = float(input("Ingrese la base del triángulo en centímetros: "))
altura_triangulo = float(input("Ingrese la altura del triángulo en centímetros: "))

# Calcular el área del triángulo: mitad base por altura
area_triangulo = (base_triangulo * altura_triangulo) / 2

# Solicitar el radio del círculo
radio_circulo = float(input("Ingrese el radio del círculo en centímetros: "))

# Calcular el área de la circunferencia: π* r² 
area_circunferencia = math.pi * (radio_circulo ** 2)

# Solicitar el ancho y altura del pecho
ancho_pecho = float(input("Ingrese el ancho del pecho en centímetros: "))
altura_pecho = float(input("Ingrese la altura del pecho en centímetros: "))

# Calcular el área del pecho: L x A
area_pecho = ancho_pecho * altura_pecho

# Solicitar el ancho y altura del brazo
ancho_brazo = float(input("Ingrese el ancho del brazo en centímetros: "))
altura_brazo = float(input("Ingrese la altura del brazo en centímetros: "))

# Calcular el área de un brazo: ancho x altura
area_brazo = ancho_brazo * altura_brazo

# Calcular el área total de ambos brazos
area_brazos = area_brazo * 2

# Solicitar el ancho y altura de la pierna
ancho_pierna = float(input("Ingrese el ancho de la pierna en centímetros: "))
altura_pierna = float(input("Ingrese la altura de la pierna en centímetros: "))

# Calcular el área de una pierna: ancho x altura
area_pierna = ancho_pierna * altura_pierna

# Calcular el área total de ambas piernas
area_piernas = area_pierna * 2

# Calcular el área total
area_total = area_triangulo + area_circunferencia + area_pecho + area_brazos + area_piernas

# Mostrar el resultado
print("El área total del nuevo muñeco de la empresa Peluchis corresponde a:", area_total, "centímetros cuadrados.")