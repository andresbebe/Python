#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Programe una funcion llamada listaReducida que reciba como parametro y cree
#una nueva a partir de ella que no incluya  el primer y ultimo elemento y luego
#la retorne.Programe
#No se puede modificar  la lista original
#Usar listas.copy()


def listaReducida(lista):

    sl = lista[1:4]
    return sl


lista=[]
for i in range(5):
    n = input ("Ingrese una lista de numeros")
    lista.append(n)

print listaReducida(lista)
