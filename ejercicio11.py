#Archivo: Ejercicio 11
#Autora: Marce Alpízar
#Fecha: 27/5/2024
#Descripción: Gabriel es un trabajador independiente que cobra 50 dólares por cada página web. Calcule los ingresos del total del mes de Gabriel. El programa recibe la cantidad de páginas web que le contrataron a Gabriel.
#solicitar
ppp = 50  # Precio por pagina
webs = float(input("Ingrese el total de páginas web trabajadas este mes: "))  # Number of web pages worked on this month

# Calculation
ingresos_mensuales = float(ppp * webs)  # Monthly earnings calculation

# Printing the result
print("El total de ganancias de este mes corresponde a: $", ingresos_mensuales)