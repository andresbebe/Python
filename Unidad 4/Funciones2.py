#!/usr/bin/env python
# -*- coding: utf-8 -*-


def arma_agenda(lista_nom, lista_tel):

#'''recibe 2 listas y retorna un diccionario'''
#Declara el diccionario , recorre nom y tel en zip (funcion que une la lista
#en una tupla), luego  por cada item de nom le pasamos tel y  retorna d

    d = {}
    for nom, tel in zip(lista_nom, lista_tel):
        d[nom] = tel
    return d

# Programa principal
#Declaracion de las dos listas n y t y cita arma_agenda con n y t
# Y pasa los valores a agenda  e imprime

n = ['Kliksberg', 'Stiglitz', 'Zaffaroni']
t = ['23444', '54556', '66554']
agenda = arma_agenda(n, t)
print(agenda)
