#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Datos de entrada
vt = input('Ingrese votos totales: ')
vop = input('Ingrese votos obtenidos por el partido: ')

vtos = vt * 1.5 / 100

re = vop >= vtos

print (re)