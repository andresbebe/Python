#!/usr/bin/env python
# -*- coding: utf-8 -*


#Este algoritmo recorre la lista de 4 elementos:
#El primer ciclo recorre y el segundo combina mediante posicion y  elemento.
#En el parentensis del segundo ciclo i + 1 responde a la posicion del elemento
# Y n al elemento en si


equipos = ["Colon", "A. Rafaela", "Central", "Newell"]
n = len(equipos)
for i in range(n):
    for j in range(i + 1, n):
        print(equipos[i],"vs",equipos[j])