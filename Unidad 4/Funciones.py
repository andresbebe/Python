#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definición de la función
def muestra_doble(x):
#'''Imprime en pantalla el doble de x'''
    print(2 * x)
# Programa principal
    a = 3.5
# invoca a la funcion
    muestra_doble(a)
    print('Todo OK')
#E imprime directamente


# Definición de la función
def calc_doble(x):
#""""Retorna el doble de x"""
    return 2 * x
# Programa principal
    a = 3.5
# invoca a la funcion en el programa principal
    doble = calc_doble(a)
    print(doble)

#Retorna el valor al programa principal y lo mete dentro de la variable doble