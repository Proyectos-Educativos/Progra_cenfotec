#Archivo: Ejercicio 8
#Autora: Marce Alpízar
#Fecha: 27/5/2024
#Descripción:El costo de un automóvil nuevo viene dado por la suma total del costo del vehículo, el porcentaje de ganancia del vendedor y de los impuestos. Si el porcentaje del vendedor es de un 10 % y el impuesto del 30%, diseñe un algoritmo que permita leer el costo del automóvil e imprimir el costo final para el consumidor.
#Solicitar el costo del automovil
costo_auto= float(input("Cuál es el precio de costo del auto?"))
#Definir variables y operaciones
ganancia_vendedor= float(costo_auto*0.01)
impuesto= float(costo_auto*0.03)
costo_total= float(costo_auto+ganancia_vendedor+impuesto)
#Resultado
print ("El costo final del auto para el consumidor es de: ", costo_total,"colones.")