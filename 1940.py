# -*- coding: utf-8 -*-
# Problema do Beecrowd: 1940 - Jogo de Estratégia

jogadores, rodadas = list(map(int,input().split())) 
jogadas = list(map(int, input().split()))

p = [None] * jogadores
for k in range(jogadores):
    p[k] = sum(jogadas[k::jogadores])
p = p[::-1]
ganhou = jogadores - p.index(max(p))
print('{}'.format(ganhou))

