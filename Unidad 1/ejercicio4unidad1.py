#!/usr/bin/env python
# -*- coding: utf-8 -*-

valori = input ("Ingrese el kilometraje del vehiculo antes de partir: ")
valorf = input ("Ingrese el kilometraje del vehiculo con el cual ha finalizado el trayecto: ")
recorridot = (valorf - valori)
print ("El trayecto total de Km es: " , recorridot)
print ("El trayecto total en metros es: ", recorridot * 100)
print ("El trayecto total en cm es: ", recorridot * 100000)