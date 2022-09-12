# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2373 - Garçom

N = int(input())
quebrados = 0

while N > 0:
    N -= 1
    L, C = list(map(int,(input()).split()))
    
    if (C < L):
        quebrados += C

print("%d"%(quebrados))
