# -*- coding: utf-8 -*-
# Problema do Beecrowd: 1933 - Tri-du

cartas = input()
palavra = cartas.split()
A = int(palavra[0])
B = int(palavra[1])

if (A >= B):    
    print("%d"%(A))
else:
    print("%d"%(B))
