#!/usr/bin/env python
# -*- coding: utf-8 -*-

varhr = input("ingrese horas: ")
varmin = input("ingrese minutos: ")
varseg = input("ingrese segundos: ")

ttsegundos = (varhr * 3600 + varmin * 60 + varseg)

#sumamos en segundos todo

dpms = (42195.0 / ttsegundos)

#dividimos 42195 metros sobre los segundos sumandos nos da metros x segundos


dpks = (dpms / 1000.0)
#distancia promedio divimos los metros x segundos por 1000 para que nos de los
#km por segundo

dpkh = (dpms * 3600) / 1000

print (ttsegundos)
print ("velocidad media en metros por segundo", dpms)
print ("velocidad media en kilometros por seg", dpks)
print ("velocidad media en kilometros por hora", dpkh)
