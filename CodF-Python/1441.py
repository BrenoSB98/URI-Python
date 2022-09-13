# -*- coding: utf-8 -*-
# Problema do Beecrowd: 1441 - Sequencia de granizo

def maior(a):
    return a != 0 and ((a & (a - 1)) == 0)

while True:
    h = int(input())
    if h == 0:
        break
    m = 0
    while maior(h) != True:
        if h > m:
            m = h
        if h % 2 == 0:
            h = int(h/2)
        else:
            h = h*3 + 1
    if h > m:
        m = h
    print("{}".format(m))
