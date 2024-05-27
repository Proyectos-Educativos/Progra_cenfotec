#Archivo: Ejercicio 3
#Autora: Marce Alpízar
#Fecha: 27/5/2024
#Descripción:Encontrar la edad de Ana dentro de diez años, si la edad de Ana es dos veces la edad de Elena. El programa recibe como entrada la edad actual de Elena, y debe imprimir la edad de Ana dentro de diez años.

#Solicitar la edad actual de Elena
edad_elena= int(input("Qué edad tiene Elena?"))
#Definir variables y operaciones
edad_ana= int(edad_elena*2)
edad_ana_futuro= int(edad_ana+10)
#Resultado
print("La edad de Ana en 10 años sera de", edad_ana_futuro)