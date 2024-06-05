#Archivo: Ejercicio 2 semana 3
#Autora: Marce Alpízar
#Fecha: 3/6/2024
#Descripción: Determinar si un ciudadano puede votar. Un ciudadano puede votar si ya cuenta con 18 años cumplidos. El programa recibe la edad del ciudadano.
votante= int(input("Ingrese su edad en años:"))
if votante>= 18:
        print("Puede votar")
else : print ("Aún no puede votar")