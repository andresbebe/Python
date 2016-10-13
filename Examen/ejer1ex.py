#!/usr/bin/env python
# -*- coding: utf-8 -*

#En un archivo de texto se tiene informacion sobre los pasajeros del titanic
#Por cada  linea del archivo se encuentran separado por comas los siguientes 5
#datos: Nombre y apellido , edad , genero (M/F) tipo de pasaje (1,2 o 3), sobre
#vivio (0 o 1 ) . Se solicita que lea este archivo e informa en pantalla lo
# siguiente : a) Cantidad de sobrevivientes b) Porcentaje de sobrevivientes
# de cada genero c) cantida de menores que sobrevivieron


archivo = open('/home/andres/Escritorio/titanic.txt', 'r')

lineas = archivo.readlines()


menores = 0
sobre = 0
ssobre = 0
sm = 0
sf = 0
ct = 0

for linea in lineas:
    nomape, edad, sexo, tp, s, x = linea.split(",")
    sobre = int(s)
    sedad = int(edad)

    if sobre == 1:
        ssobre = ssobre + 1
        if sexo == "M":
            sm = sm + 1
        if sexo == "F":
            sf = sf + 1
        if sedad < 10:
            menores = menores + 1

porcentajem = ((sf * 100.0) / ssobre)
porcentajef = ((sm * 100.0) / ssobre)

print ("La cantidad de sobrevivientes", ssobre)

print sm
print sf
print menores

print ("Porcentajes de hombres sobrevivientes", porcentajef)
print ("Porcentajes de mujeres sobrevivientes: ", porcentajem)
#print ("")


