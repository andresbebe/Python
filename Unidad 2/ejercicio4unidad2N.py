#!/usr/bin/env python
# -*- coding: utf-8 -*

votost = input ("Ingrese los votos totales: ")
votosp = input ("Ingrese los votos sacados por el partido: ")

porvp = (votosp * 100.0) / votost

generales = porvp >= 1.5

print ("Cantidad de votos validos: ", votost)
print ("Cantidad de votos obtenidos: ", votosp)
print ("Porcentaje de votos: ", porvp)

print ("Participa de las generales", generales)