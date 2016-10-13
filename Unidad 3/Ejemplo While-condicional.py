#!/usr/bin/env python
# -*- coding: utf-8 -*

#Ejemplo de estructura , mientras se cumpla la condicion
#se mantendra dentro del ciclo, si no  sale.Ejemplo
#En este caso mientras vez sea <= 5 se ejecutara lo siguiente
#En cuanto vez es mayor en el contador vez = vez + 1 sale.
#La variable vez se inicializa en 1
#Cada vez que se ejecuta se cuenta en vez = vez + 1

vez = 1
while vez <= 3:
    temperatura = int(input('Ingrese la temperatura en oC:'))
    if (temperatura > 16):
        print('Vas caminando')
    else:
        print('Mucho frío, en vehículo')
    vez = vez + 1