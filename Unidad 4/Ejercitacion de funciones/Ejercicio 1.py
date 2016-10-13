#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Definir una función max() que tome como argumento dos números y devuelva
# el mayor de ellos. (Es cierto que python tiene una función max()
#incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.


def fmax(n1, n2):
    if n1 < n2:
        print ("n2 es mayor que n1")
    elif n1 == n2:
        print ("n2 es igual a n1")
    elif n1 > n2:
        print ("n1 es mayor a n2")

#Programa principal

fmax(3, 6)