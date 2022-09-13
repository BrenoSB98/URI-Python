# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2344 - Notas de Prova

n = int(input())

#Converter as notas
if (n == 0):
    print ("E")

if (n >= 1) and (n <= 35):
    print("D")

if (n >= 36) and (n <= 60):
    print("C")

if (n >= 61) and (n <= 85):
    print("B")

if (n >= 86) and (n <= 100):
    print("A")

