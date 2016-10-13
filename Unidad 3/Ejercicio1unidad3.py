#!/usr/bin/env python
# -*- coding: utf-8 -*

#Con el siguiente fragmento de programa se puede determinar si una letra es vocal:
#if letra in ("aeiou"):
#print("Es vocal!")
#Realice un programa que permita ingresar una palabra y finalmente informe la cantidad de vocales que
#posee. Una vez finalizado el ejercicio, se lo desafía a extenderlo para que contabilice la repetición de
#cada vocal.


vocales = "aeiou"
cantv = 0
canta = 0
cante = 0
canti = 0
canto = 0
cantu = 0
cantl = 0

palabra = raw_input("Ingrese la palabra a revisar:")

for letra in palabra:
    cantl = cantl + 1
    for vocal in vocales:
        if vocal == letra:
            cantv = cantv + 1
            if vocal == "a":
                canta = canta + 1
            elif vocal == "e":
                cante = cante + 1
            elif vocal == "i":
                canti = canti + 1
            elif vocal == "o":
                canto = canto + 1
            elif vocal == "u":
                cantu = cantu + 1

print ("La cantidad de letras en la palabra", cantl)
print ("La cantidad de vocales totales es:", cantv)
print ("La cantidad de vocales a", canta)
print ("La cantidad de vocales e", cante)
print ("La cantidad de vocales i", canti)
print ("La cantidad de vocales o", canto)
print ("La cantidad de vocales u", cantu)



