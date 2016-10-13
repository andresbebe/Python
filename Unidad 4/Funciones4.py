#!/usr/bin/env python
# -*- coding: utf-8 -*-


def contar_pares(num):
    global pares
    if num % 2 == 0:
        pares = pares + 1
pares = 0

#Programa principal

contar_pares(2)
contar_pares(5)
contar_pares(8)
print(pares)