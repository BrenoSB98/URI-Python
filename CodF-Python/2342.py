# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2342 - Overflow

n = int(input())

linha = input()
palavra = linha.split()
valor_1 = int(palavra[0])
valor_2 = str(palavra[1])
valor_3 = int(palavra[2])

if valor_2 == "+":
    resultado = valor_1 + valor_3
else:
    resultado = valor_1 * valor_3

if resultado > n:
    print("OVERFLOW")
else:
    print("OK")
