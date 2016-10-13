#!/usr/bin/env python
# -*- coding: utf-8 -*

#Lista vacia

vacia = []

#Lista con 3 valores flotantes

tempC = [12.2, 33.3, 12.1]

# Elemento 1 de la lista

print("2do elemento:", tempC[1])

# Reemplaza el elemento 1 con 100

tempC[1] = 100

print("2do elemento modificado:", tempC[1])

# Lista completa y calculo de promedio

print("Lista:")

media = 0.0

for i in tempC:
    print(i)
media = media + i
media = media / 3

# Elementos que superan el promedio

for i in tempC:
    if i > media:
        print("La temperatura", i, "supero la media")