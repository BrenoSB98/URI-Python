# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2670 - Máquina de Café


predio = []
for i in range (3): #Ler quantidade de pessoas por andares
    predio.append(int(input()))
tempo = []
# Calcular menor tempo
for i in range(3):
    tempo.append(predio[0]*4 + predio[1]*2)
    tempo.append(predio[0]*2 + predio[2]*2)
    tempo.append(predio[1]*2 + predio[2]*4)
tempo.sort()
#Escreva tempo na posição 1
print(tempo[1])
