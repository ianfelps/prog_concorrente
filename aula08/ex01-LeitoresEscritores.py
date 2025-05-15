'''
Implementação do problema dos leitores e escritores, usando o módulo threading e considerando a política "preferência para leitores", ou seja, leitores podem acessar simultaneamente, enquanto escritores precisam de acesso exclusivo.
'''

import threading
import time
import random

# recursos compartilhados
leitores_ativos = 0
lock_leitor = threading.Lock() # protege leitores_ativos
lock_acesso = threading.Lock() # protege acesso ao recurso compartilhado

# dados fictícios (o "recurso compartilhado")
dados = {"valor": 0}

# função do leitor
def leitor(id_leitor):
    global leitores_ativos
    
    while True:
        # entrada da seção crítica dos leitores
        with lock_leitor:
            leitores_ativos += 1
            if leitores_ativos == 1:
                lock_acesso.acquire() # primeiro leitor bloqueia escritores
        
        # leitura (simulada)
        print(f"[Leitor {id_leitor}] lendo: {dados['valor']}")
        time.sleep(random.uniform(0.1, 0.5))
        
        # saída da seção crítica dos leitores
        with lock_leitor:
            leitores_ativos -= 1
            if leitores_ativos == 0:
                lock_acesso.release() # último leitor libera escritores
        
        time.sleep(random.uniform(0.5, 1.5))

# função do escritor
def escritor(id_escritor):
    while True:
        lock_acesso.acquire() # escritor precisa de exclusividade
        # escrita (simulada)
        novo_valor = random.randint(1, 100)
        print(f" [Escritor {id_escritor}] escrevendo: {novo_valor}")
        dados["valor"] = novo_valor
        time.sleep(random.uniform(0.2, 0.6))
        
        lock_acesso.release() # libera para leitores/escritores
        time.sleep(random.uniform(1, 2))
    
# criar threads de leitores e escritores
for i in range(3): threading.Thread(target=leitor, args=(i,), daemon=True).start()
for i in range(2): threading.Thread(target=escritor, args=(i,), daemon=True).start()
    
# manter programa principal ativo
time.sleep(15)