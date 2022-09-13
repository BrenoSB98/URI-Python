# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2235 - Andando no tempo

a, b, c = map(int,input().split()) #Ler créditos

#Calculo para saber se é possível voltar ao presente
if (a - b == 0) or (a - c == 0) or (b - c == 0):
    print('S')
elif (a + b - c == 0) or (a + c - b == 0) or (b + c - a == 0):
    print('S')
else:
    print('N')
