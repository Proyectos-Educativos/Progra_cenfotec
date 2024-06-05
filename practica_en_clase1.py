#Archivo: Ejercicio 1 semana 3
#Autora: Marce Alpízar
#Fecha: 3/6/2024
#Descripción:Dado el salario bruto y la cantidad de camisas vendidas por un empleado que trabaja en una empresa de venta de camisas, calcular el salario neto teniendo en cuenta los siguientes factores: ● Se debe restar un 8%del salario bruto para cubrir el seguro de salud. ● Se debe restar un 12% adicional por concepto de impuesto de renta. ● La empresa paga regalías por cada venta realizada por el empleado. El porcentaje de las regalías es del 3% sobre el total de las ventas.

salario_bruto = float(input("Ingrese el salario bruto del empleado: "))
cantidad_camisas = int(input("Ingrese la cantidad de camisas vendidas: "))
seguro_salud= float(salario_bruto * 0.08)
imp_renta= float(salario_bruto * 0.12)
regalia= float (salario_bruto *0.03)

salario_neto= float(salario_bruto-seguro_salud-imp_renta+regalia)
print("El salario neto después de deducciones y regalías corresponde a: ", salario_neto)