# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2296 - Trilhas

import sys

# n <- Número total de trilhas
n = int(input())

# Variaveis para resolução
menor_trilha = sys.maxsize
indice_final = -1
cont = 0 # Variavel contadora

# Primeiro verifica se existem trilhas e se são menores que o valor maximo
if n > 0 and n <= 100:
    # Lendo a quantidade de Pontos e suas respectivas alturas
    while cont < n:
        quant_pontos = input()
        aux_pontos = quant_pontos.split()
        m = int(aux_pontos[0])
        altura = []

        # Laço auxiliar para alocar as alturas no vetor altura
        for j in range(1, m + 1):
            altura.append(int(aux_pontos[j]))

        # Laço que verificar o esforco de esforco_ida
        esforco_ida = 0
        for k in range(0, m-1):
            desnivel_ida = altura[k + 1] - altura[k]
            
            if desnivel_ida > 0:
                esforco_ida += desnivel_ida

        # Laço para calcular o desnivel de volta
        esforco_volta = 0
        for l in range(m-1, 0, -1):
            desnivel_volta = altura[l-1] - altura[l]
            
            if desnivel_volta > 0:
                esforco_volta += desnivel_volta
        
        # Analisando qual esforço é maior
        if esforco_ida < esforco_volta:
            menor_atual = esforco_ida
        else:
            menor_atual = esforco_volta
        
        # Analisando qual a menor trilha
        if menor_atual < menor_trilha:
            menor_trilha = menor_atual
            indice_final = cont
        cont += 1

print(f'{indice_final + 1}')
