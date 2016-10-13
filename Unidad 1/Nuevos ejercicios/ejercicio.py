#!/usr/bin/env python
# -*- coding: utf-8 -*-

drecorridakm = input ("ingrese los km: ")
varhr = input("ingrese horas: ")
varmin = input("ingrese minutos: ")
varseg = input("ingrese segundos: ")


ttsegundos = (varhr * 3600 + varmin * 60 + varseg)

dametros = drecorridakm * 1000.0

dpms = (dametros / ttsegundos)

dpks = (dpms / 1000.0)

dpkh = (dpms * 3600) / 1000

print (ttsegundos)
print ("velocidad media en metros por segundo", dpms)
print ("velocidad media en kilometros por seg", dpks)
print ("velocidad media en kilometros por hora", dpkh)
