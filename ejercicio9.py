#Archivo: Ejercicio 9
#Autora: Marce Alpízar
#Fecha: 27/5/2024
#Descripción: Vilma Picapiedra envía a Pedro a comprar el pan, le jamón, el queso, el tomate y la lechuga para hacer el almuerzo del domingo. Vilma le entregó a Pedro 10 mil colones, y regresó con 2700. Cuando Vilma le preguntó cuánto le costó cada cosa, Pedro le contesta que el pan le costó un 15 %, el tomate un 35 %, el queso y el jamón ambos un 20 % y la lechuga un 10%. Haga un programa que calcule el costo en colones de cada ingrediente.

#Información dada
billete= 10000
vuelto= 2700
porcentaje_pan = 0.15
porcentaje_jamon = 0.20
porcentaje_queso = 0.20
porcentaje_tomate = 0.35
porcentaje_lechuga = 0.10

#monto gastado por Pedro
gasto_total= billete-vuelto

#operaciones calculo cada ingrediente
costo_pan = gasto_total * porcentaje_pan
costo_jamon= gasto_total* porcentaje_jamon
costo_queso = gasto_total * porcentaje_queso
costo_tomate = gasto_total * porcentaje_tomate
costo_lechuga = gasto_total * porcentaje_lechuga

#Resultado
print ("El costo del pan corresponde a: ", costo_pan, "colones." "El costo del jamón corresponde a: ", costo_jamon, "colones." "El costo del queso corresponde a: ", costo_queso, "colones." "El costo del tomate corresponde a: ", costo_tomate, "colones.""El costo de la lechuga corresponde a: ", costo_lechuga, "colones.")


