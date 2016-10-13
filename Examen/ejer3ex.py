#!/usr/bin/env python
# -*- coding: utf-8 -*

#Realice un programa que permita calcular el monto acumulado luego de hacer un
#deposito a plazo fijo. El programa permite  ingresar una cantidad de pesos,
#una tasa de interes anual y un numero de meses.
#El programa debe mostrar por pantalla en cuanto se habra convertido el capital
#inicial transcurridos ese periodo de tiempo ( expresado en meses ) Tenga
#En cuenta que la unidad de medida no es años si no meses.
#Por ejemplo:
#    capital inicial : $1000
#    Tasa anual (%): 12
#    Periodo en meses: 3
#    Capital acumulado:1030 (1000 iniciales + 30 de interes

m = input("Ingrese el monto del deposito a plazo fijo")
t = input("Ingrese la tasa de interes anual")
p = input("Ingrese el periodo en meses")

res = ((((m * t) / 100.0 ) / 12 ) * p) + m

print res