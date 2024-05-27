#Archivo: Ejercicio 2
#Autora: Marce Alpízar
#Fecha: 24/5/2024
#Descripción:Calcular la cantidad de kilómetros de un viaje realizado en carro. El algoritmo debe recibir el kilometraje del vehículo antes de iniciar el viaje, y el kilometraje del vehículo al terminar el viaje. Se debe imprimir el total de kilómetros del viaje.

#Solicitar el kilometraje actual o inicial
kilometraje_inicial= float(input("Cuál es el kilometraje inicial antes del viaje?"))
kilometraje_final= float(input("Cuál es  el kilometraje final después del viaje?"))

#Definir variables y operaciones
kilometros_total_viaje= float(kilometraje_final- kilometraje_inicial)
#Resultado
print("La cantidad de kilometros recorridos en el viaje es de", kilometros_total_viaje)
