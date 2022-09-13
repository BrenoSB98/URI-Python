# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2437 - Distancia de Manhattan

coordenadas = input()
palavra = coordenadas.split()
Xm = int(palavra[0])
Ym = int(palavra[1])
Xr = int(palavra[2])
Yr = int(palavra[3])

distancia = abs(Xr - Xm) + abs(Yr - Ym)

print("%d"%(distancia))
