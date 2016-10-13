#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejercicio 3: Se ingresan por teclado una serie de 5 valores de temperaturas
#pronosticados para una semana.
#Se solicita
#que los almacene en una lista y utilice una función que retorne el tipo
#de alerta a emitir según lo siguiente:
#• Verde: en ningún día de los siguientes cinco consecutivos,
#sea superada las temperatura de 30 °C.
#• Amarillo: que 1 o 2 de los siguientes cinco días consecutivos,
#sea superada la temperatura de 30 °C
#• Naranja: se espera que 3 o 4 de los cinco días consecutivos
#se supere la temperatura de 30 °C
#• Rojo: cuando se espera que en cada uno de los cinco días se supere los 30 °C
#Una vez retornado el tipo de alerta el programa debe dar un mensaje alusivo..

def alerta(valores):
    dv = 0
    da = 0

    for i in valores:
        if i <= 30:
            dv = dv + 1

    for j in valores:
        if i >= 30:
            da = da + 1

    if dv == 5:
        return "Alerta Verde"
    if da >= 1 and da <= 2:
        return "Alerta Amarilla"
    if da >= 3 and da <= 4:
        return "Alerta Naranja"
    if da == 5:
        return "Alerta Roja"


v = 0
valores = []
for i in range(5):
    v = input ("Ingrese los valores de las temperaturas")
    valores.append(v)
print valores

print alerta(valores)




