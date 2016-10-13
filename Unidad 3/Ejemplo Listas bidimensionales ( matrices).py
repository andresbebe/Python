#!/usr/bin/env python
# -*- coding: utf-8 -*


#El acceso a cada dato se realiza utilizando los dos índices, donde el primero
#hace referencia a la fila y el segundo a la columna. Así, si se accede al
#segundo elemento (columna 1) de la tercer fila sería (fila 2):matriz[2][1].

#NOTA: en el caso de los for anidados recorre de izquierda a derecha la matriz
#Establece la posicion 0,0  antes de imprimir el valor, en este codigo
#por cada vez que recorra la fila recorrera 3 veces la columna

#Recordemos fila-columna

matriz = [
[12.2, 33.3, 12.1, 0.3, 1.21],
[3.14, 2.1, 9.8, 28.1, 19.9],
[10.8, 0.1, 0.2, 22.1, 9.38]
]

for c in range(5):
    print("Columna",c)
    for f in range(3):
        print(matriz[f][c])
    print()