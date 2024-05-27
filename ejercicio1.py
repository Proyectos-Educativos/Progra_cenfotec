#Archivo: Ejercicio 1 
#Autora: Marce Alpízar
#Fecha: 24/5/2024
#Descripción: Calcular el precio final de cualquier producto, si se sabe que la tasa de impuesto al valor agregado es de un 13 %. El algoritmo debe recibir el nombre del producto y el precio, y debe imprimir el nombre del producto y el precio final. Para los efectos del ejercicio, TODOS los productos pagan impuesto.

#Solicitar nombre del producto y el precio bruto
nombre_producto= (input("Cuál es el nombre del producto?"))
precio_inicial= float(input("Cuál es el precio bruto?"))

#Definir variables y operaciones
iva= float(precio_inicial*0.13)
precio_final= float( precio_inicial + iva)
#Resultado
print("El precio total de", nombre_producto, "es de", precio_final,)