# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2295 - Frota de Taxi

valor = input()
palavra = valor.split()
A = float(palavra[0])
G = float(palavra[1])
Ra = float(palavra[2])
Rg = float(palavra[3])

if ( Ra / A ) <= ( Rg / G ):
    print('G')
else:
    print('A')

