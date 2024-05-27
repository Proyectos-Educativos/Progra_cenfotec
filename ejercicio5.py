#Archivo: Ejercicio 5
#Autora: Marce Alpízar
#Fecha: 27/5/2024
#Descripción:Hugo, Paco y Luis decidieron vender limonada en el barrio. Decidieron cobrar por cada limonada 10 colones debido a que fabricar cada limonada les cuesta 5.50 colones. Como no todos trabajaron por igual, decidieron que las ganancias se iban a repartir de la siguiente forma 30 % para Paco, 30 % para Luis y 40 % para Hugo. Haga un programa que reciba la cantidad total de limonadas que vendieron, e imprima cuánto ganó Hugo, cuánto ganó Paco y cuánto ganó Luis.
#Solicitar el total de limonadas vendidas
limonadas_vendidas= int(input("Cuantas limonadas se vendieron en total?"))
#Definir variables y operaciones
ganancia_por_unidad= float(10-5.50)
total_ganancias= float(limonadas_vendidas*ganancia_por_unidad)
ganancia_paco= float(total_ganancias*0.3)
ganancia_luis= float(total_ganancias*0.3)
ganancia_hugo= float(total_ganancias*0.4)
#Resultado
print ("La ganancia de Paco corresponde a", ganancia_paco,"colones.", "La ganancia de Luis corresponde a", ganancia_luis,"colones.","La ganancia de Hugo corresponde a", ganancia_hugo,"colones.")