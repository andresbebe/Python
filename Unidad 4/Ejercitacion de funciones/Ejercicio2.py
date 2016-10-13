#!/usr/bin/env python
# -*- coding: utf-8 -*-

#2- Definir una función max_de_tres(), que tome tres números como argumentos
# y devuelva el mayor de ellos.


def maxdetres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print ("El mayor es n1")
    elif n2 > n1 and n2 > n3:
        print ("El mayor es n2")
    elif n3 > n2 and n3 > n1:
        print ("El mayor es n3")
    elif n3 == n2 and n3 == n1:
        print ("Son todos iguales")
    elif n2 == n1 or n3 == n2:
        print ("No se puede saber uno es igual a otro")

#Programa principal

maxdetres(4, 5, 9)