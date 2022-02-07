# -*- coding: utf-8 -*-
# Problema do Uri Online Judge: 2286 - Par ou Impar

# n <- O número de Partidas
n = int(input())

# Teste é o contador do número de testes, começando em 1
teste = 1

# Enquanto Verdadeiro, ou seja, n != 0
while True:
    if n > 0:
        #Inicializa os nomes dos jogadores
        nome_par = input()
        nome_impar = input()
        
        # Verificando se os nomes dos jogadores estão dentro do padrão
        if len(nome_par) < 1 or len(nome_impar) < 1 or len(nome_par) > 10 or len(nome_impar) > 10:
            break
        else:
            print(f'Teste {teste}')
            
            # Iniciando os Testes
            for i in range(n):
                # Transformando a string em inteiros
                valores_jogados = input()
                valores = valores_jogados.split()
                valor_jp = int(valores[0])
                valor_ji = int(valores[1])

                # Somando a jogada os dois jogadores e verificando quem venceu
                soma = valor_jp + valor_ji

                if not soma % 2 == 0:
                    print(f'{nome_impar}')
                else:
                    print(f'{nome_par}')
            print()
    else:
        if n == 0:
            break
    teste += 1
    n = int(input())
