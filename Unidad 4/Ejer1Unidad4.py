#!/usr/bin/env python
# -*- coding: utf-8 -*-

#1 . Escriba una función que reciba como parámetro la temperatura
#expresada en grados centígrados (oC) e imprima en pantalla la misma
#temperatura en grados Fahrenheit (oF). Tenga en cuenta que la formula
#de conversión de Celsius a Fahrenheit es la siguiente:
#F =(9C=5:0) +32


def pasajegrados(t):
    f = 9 / 5.0* t + 32
    return f

g = input ("Ingrese el valor en grados Centigrados: ")
print pasajegrados(g)