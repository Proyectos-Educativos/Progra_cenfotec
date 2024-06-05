#Archivo: Ejercicio 1 semana 3
#Autora: Marce Alpízar
#Fecha: 3/6/2024
#Descripción:Dada una cantidad de bits, se desea calcular la cantidad equivalente en gigabytes GB.

#informacion necesitaria: 1GB es igual a 1024MG, 1MG es igual a 1024kb, 1kb es igual a 1024B, 1B es 8 bits.
#Solicitar input
bits= int(input("Ingrese cantidad de bits:"))
#operacion: conversion indirectas
GB= bits/ (8*1024*1024*1024)
#Resultado
print(" ", bits, "equivale a:", GB, "Gigabytes")

