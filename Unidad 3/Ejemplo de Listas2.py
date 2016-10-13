#!/usr/bin/env python
# -*- coding: utf-8 -*

#Lista vacia

vacia = []

#Lista con 3 valores flotantes

tempC = [12.2, 33.3, 12.1]

#Lista que almacena distintos tipos de datos
popurri = [12, 3.1415, "amapola del 66", True, tempC]

#Imprimen los elementos

print ("1er elemento: ", popurri[0])
print ("2do elemento: ", popurri[1])
print ("3er elemento: ", popurri[2])
print ("4to elemento: ", popurri[3])
print ("5to elemento: ", popurri[4])

#Para poder manipular los elementos de una lista dentro de otra , en temp
# el elemento 4 de la primera lista especificamemos el elementos a mostrar

print(popurri[4][0])
print(popurri[4][1])
print(popurri[4][2])

#Para saber la cantidad de elementos que hay en una lista y en la lista dentro
#de la otra.

print(len(popurri))
print(len(popurri[4]))


# Usar len para contar la cantidad de elementos y recorrerlo con un for

n = len(tempC)
for i in range(n):
    print("Temperatura", i, ":", tempC[i])