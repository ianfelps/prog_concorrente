# algoritmo para calcular variancia (com paralelismo)

import time
import random
import threading

# função para somar quadrados
def somarQuadrados(dados, media):
    soma = 0
    for x in dados:
        soma += (x - media) ** 2
    return soma

# função para calcular variancia
def calcularVariancia(dados):
    # calcular a media dos elementos
    N = len(dados) # pega o numero de elementos do vetor
    # dividir lista dos dados em 2
    meio = N // 2
    media = sum(dados) / N # calcular a media
    esquerda = dados[:meio]
    direita = dados[meio:]
    # calcular a soma dos desvios quadrados
    sq_esquerda = 0
    sq_direita = 0
    # funcao para processar dados da esquerda
    def processarEsquerda():
        nonlocal sq_esquerda
        sq_esquerda = somarQuadrados(esquerda, media)
    # funcao para processar dados da direita
    def processarDireita():
        nonlocal sq_direita
        sq_direita = somarQuadrados(direita, media)
    # iniciar threading
    thread_esquerdo = threading.Thread(target = processarEsquerda)
    thread_direito = threading.Thread(target = processarDireita)
    thread_esquerdo.start()
    thread_direito.start()
    thread_esquerdo.join()
    thread_direito.join()
    # juntar soma dos quadrados e dividir pelo numero de elementos
    sq_total = sq_esquerda + sq_direita
    variancia = sq_total / N
    return variancia
    

# exemplo de uso

lista1 = [2, 4, 6, 8, 10] # var = 8
lista2 = [2, 3, 4, 5, 6] # var = 2
lista3 = [2, 2, 2, 2, 2] # var = 0

lista = [random.randint(1, 100) for _ in range(10000000)] # gerar lista com 10M de elementos aleatórios

t0 = time.time()
print(f"Variância = {calcularVariancia(lista)}")
tf = time.time()
print(f"Tempo de execução: {tf - t0} segundos") # 2.04 s