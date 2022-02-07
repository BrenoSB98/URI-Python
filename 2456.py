# -*- coding: utf-8 -*-
# Problema do Uri Online Judge: 2456 - Cartas

# Lendo os valores das cartas e colocando no array
cartas = [int (i) for i in input().split()]

if cartas == sorted(cartas):
    print('C')
elif cartas == sorted(cartas, reverse=True):
    print('D')
else:
    print('N')
