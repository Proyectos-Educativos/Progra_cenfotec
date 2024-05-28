#Archivo: Ejercicio 7
#Autora: Marce Alpízar
#Fecha: 27/5/2024
#Descripción:Johns Hopkins University Center for Systems Science and Engineering lleva un recuento de la cantidad de casos y la cantidad de muertes a nivel mundial por el Covid-19. Haga un programa que reciba el nombre del país, la cantidad de enfermos, la cantidad de muertos e imprima la tasa de mortalidad para dicho país.
#Solicitar el país, cantidad de enfermos, cantidad de muertos
pais =(input("Ingrese el nombre del país: "))
fallecidos = int(input("Ingrese el número de personas fallecidas:"))
enfermos = int(input("Ingrese el número de personas enfermas: "))

#Definir variables y operaciones
tasa_mortalidad= int(fallecidos / enfermos*100)
#Resultado
print ("En", pais,"la tasa de mortalidad corresponde a: ", tasa_mortalidad,"%.")
