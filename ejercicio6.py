#Archivo: Ejercicio 6
#Fecha: 27/5/2024
#Descripción:Con la situación del Covid-19, el Gobierno decidió poner un impuesto al salario bruto de todos los trabajadores. Haga un programa que reciba el porcentaje de impuesto y el salario bruto de un trabajador, e imprima lo que le queda luego de rebajar el impuesto.
#Solicitar el salario bruto del colaborador y el impuesto porcentual a deducir
salario_bruto =float(input("Cuál es el salario bruto de la persona colaboradora? "))
impuesto_porcentual=float(input("Cuál es el porcentaje a deducir? "))
#Definir variables y operaciones
total_impuesto_deducir= float(impuesto_porcentual/100)*salario_bruto
salario_neto= float(salario_bruto-total_impuesto_deducir)
#Resultado
print("El total de salario a pagar luego de la deducción corresponde a:", salario_neto,"colones.")