# -*- coding: utf-8 -*-
# Problema do Beecrowd: 2782 - Escadinha

n = int(input())
t = 1

v = list(map(int,input().split()))
for i in range (2, len(v)):
    if (v[i] - v[i - 1] != v[i - 1] - v[i - 2]):
        t += 1
print("{}".format(t))
