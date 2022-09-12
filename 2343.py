# -*- coding: utf-8 -*-
# Problema Beecrowd: 2343 - Caçadores de Mitos

n = int(input())
mapa = [None] * 501
for y in range(501):
    mapa[y] = [False] * 501
mito = 0

for _ in range(n):
    x, y = map(int, input().split())

    if mapa[y][x]:
        mito = 1
        break
    else:
        mapa[y][x] = True
print(mito)