#Archivo: Ejercicio 4
#Autora: Marce Alpízar
#Fecha: 27/5/2024
#Descripción: Encontrar la edad de la abuela de Ana a hoy, si es 7 años menor que el abuelo de Ana, y en el año del matrimonio, el abuelo tenía 25 años. El programa recibe como entrada el año del matrimonio.
#Solicitar el año de matrimonio
anho_matrimonio= int(input("En qué año se casaron los abuelos de Ana?"))
anho_actual= 2024
#Definir variables y operaciones
edad_abuelo= int (anho_actual-anho_matrimonio)+25
edad_abuela= int (edad_abuelo-7)
##Es necesario importar las depencendias necesarias pero no sé como#

#Resultado
print ("La edad de la abuela de Ana es de", edad_abuela)