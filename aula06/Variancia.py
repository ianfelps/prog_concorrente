# algoritmo para calcular variancia (sem paralelismo)

import time
import random

# função para calcular variancia
def calcularVariancia(dados):
    # calcular a media dos elementos
    N = len(dados) # pega o numero de elementos do vetor
    soma = 0
    for x in dados: # soma todos os elementos
        soma += x
    media = soma / N # divide pelo numero de elementos
    # calcular a soma dos desvios quadrados
    soma_dq = 0
    for x in dados: # soma os valores subtraidos pela media e eleva a 2
        soma_dq += (x - media) ** 2
    variancia = soma_dq / N # divide pelo numero de elementos
    # retorna o resultado
    return variancia

# exemplo de uso

lista1 = [2, 4, 6, 8, 10] # var = 8
lista2 = [2, 3, 4, 5, 6] # var = 2
lista3 = [2, 2, 2, 2, 2] # var = 0

lista = [random.randint(1, 100) for _ in range(10000000)] # gerar lista com 10M de elementos aleatórios

t0 = time.time()
print(f"Variância = {calcularVariancia(lista)}")
tf = time.time()
print(f"Tempo de execução: {tf - t0} segundos") # 2.31 s