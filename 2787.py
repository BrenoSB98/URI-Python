# -*- coding: utf-8 -*-
# Problema do Uri Online Judge: 2787 - Xadrez

# Lendo quantas linhas e colunas que há no tabuleiro de xadrez.
linhas_tabuleiro = int(input())
colunas_tabuleiro = int(input())

if 1 <= linhas_tabuleiro and linhas_tabuleiro <= 1000 and 1 <= colunas_tabuleiro and colunas_tabuleiro <= 1000:
    
    # Verificando se a casa do tabuleiro é branca ou preta
    if (linhas_tabuleiro + colunas_tabuleiro)%2 == 0:
        print('1')
    else:
        print('0')
else:
    print('ERRO')
