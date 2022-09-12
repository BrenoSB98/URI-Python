# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2187 - Bits Trocados

# V <- O valor solicitado pelo cliente.
V = int(input())

# Iniciando variaveis para ajudar na resolução
I = 0   # I refere-se a nota de B$ 50
J = 0   # J refere-se a nota de B$ 10
K = 0   # K refere-se a nota de B$ 5
L = 0   # L refere-se a nota de B$ 1
n = 1   # N <- Número do teste atual

# Enquanto o valor solicitado pelo cliente não
# estiver sacado por completo
while V != 0:

    # O caixa eletronico seleciona as notas necessárias
    # Verificando quantas notas de 50 são necessárias
    I = V//50
    V = V%50

    # Verificando quantas notas de 10 são necessárias
    J = V//10
    V = V%10

    # Verificando quantas notas de 5 são necessárias
    K = V//5
    V = V%5

    # Verificando quantas notas de 1 são necessárias
    L = V

    # Saidas
    # Número do teste
    print(f'Teste: {n}')

    # Quantas notas de cada são necessárias
    print(f'{I} {J} {K} {L}')
    print()
    
    n += 1
    V = int(input())
