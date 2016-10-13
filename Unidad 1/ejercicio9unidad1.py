#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Datos de entrada
equipo_a = input('Cantidad de hinchas del equipo A: ')
equipo_b = input('Cantidad de hinchas del equipo B: ')
costo_picada = input('Costo de la picada: ')
costo_cervezas = input('Costo total de las cervezas: ')

# Sumo los costos
costo_total = float(costo_picada) + float(costo_cervezas)
# Sumo los equipos
equipo_total =  int(equipo_b) + int(equipo_a)

# Para el caso en que gane el equipo A
monto_a_pagar = costo_total / int(equipo_b)
print('Si el equipo B pierde, sus hinchas deben pagar: $', monto_a_pagar)

# Para el caso en que gane el equipo B
monto_a_pagar = costo_total / int (equipo_a)
print('Si el equipo A pierde, sus hinchas deben pagar: $', monto_a_pagar)

# Para el caso de que empate equipo A y equipo B

monto_a_pagar = costo_total / equipo_total
print('Si el equipo A empata con el equipo B: $', monto_a_pagar)