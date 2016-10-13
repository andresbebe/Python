#!/usr/bin/env python
# -*- coding: utf-8 -*

temperatura = int(input('Ingrese la temperatura en oC: '))
distancia = int(input('Ingrese la distancia a recorrer en km: '))
if 10 < temperatura < 30:
#1er condicional
    if distancia <= 15:
#2do condicional
        print('Lindo clima para ir en bici')
    else:
        print('Es lejos, te recomiendo cole')
else:
    print('No está agradable, recomiendo cole')
    print('Que tenga buen día!')