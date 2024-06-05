#Archivo: Ejercicio 8 semana 3
#Autora: Marce Alpízar
#Fecha: 5/6/2024
##Descripción: Una empresa que vende flores sacó una promoción, si el cliente compra tres flores, le aplica un descuento del 10%. El programa recibe la cantidad de flores y el precio de cada flor. Se debe imprimir el total a pagar.

cantidad_flores= int(input("Cuantas flores compró?"))
precio_flores= int(input("Cuanto cuesta cada flor?"))
total= (cantidad_flores*precio_flores)
descuento= (total*0.10)
total_con_descuento= (total-descuento)

if (cantidad_flores==3):
    print("El total a pagar con descuento corresponde a:",total_con_descuento )
else:
    print("El total a pagar sin descuento corresponde a:", total)
    
