#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escriba una función que reciba como parámetro la temperatura expresada
#en grados centígrados (oC) e imprima en pantalla la misma temperatura en grados
#Fahrenheit (oF). Tenga en cuenta que la formula de conversión de Celsius a
#Fahrenheit es la siguiente: F =(9C=5:0) +32


def conversion_grados(valor):
    f = (9 / 5.0 * n) + 32
    return f



#Programa principal

n = int(input ("Ingrese el valor a convertir: "))
grados = conversion_grados(n)
print ("En grados Farenheit es: ", grados)


