#Archivo: Ejercicio 10
#Autora: Marce Alpízar
#Fecha: 27/5/2024
#Descripción:Una línea aérea pone en promoción los viajes a África. La promoción indica que el costo del tiquete tendrá una rebaja del 15 %. Imprima el costo real del tiquete si el programa recibe el precio original del mismo.

#Solicitar el precio original del mismo
tiquete= float(input("Ingrese el precio original del tiquete "))
#Definir variables y operaciones
descuento= float(tiquete*0.15)
precio_con_descuento= float(tiquete-descuento)
#Resultado
print("El precio del tiquete a Africa con un 15% de descuento es de: ", precio_con_descuento)