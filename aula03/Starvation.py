import threading
import time

# Variáveis globais para rastrear o uso do recurso
high_priority_count = 0
low_priority_count = 0

# Cria um lock para controlar o acesso ao recurso compartilhado
resource_lock = threading.Lock()

# Função executada pela thread de alta prioridade
def high_priority_thread():
    global high_priority_count
    while True:
        with resource_lock: # Adquire o lock
            print("[ALTA PRIORIDADE] Usando o recurso...")
            high_priority_count += 1
            time.sleep(0.9) # Simula uso prolongado do recurso

# Função executada pela thread de baixa prioridade
def low_priority_thread():
    global low_priority_count
    while True:
        with resource_lock: # Tenta adquirir o lock
            print("[BAIXA PRIORIDADE] Conseguiu usar o recurso!")
            low_priority_count += 1
            time.sleep(0.1) # Simula uso rápido do recurso

# Cria as threads
high_priority = threading.Thread(target=high_priority_thread, daemon=True)
low_priority = threading.Thread(target=low_priority_thread, daemon=True)

# Inicia as threads
high_priority.start()
low_priority.start()

# Monitora o uso do recurso por 10 segundos
time.sleep(10)

# Relatório final
print("\n--- RELATÓRIO FINAL ---")
print(f"Thread de Alta Prioridade usou o recurso {high_priority_count} vezes.")
print(f"Thread de Baixa Prioridade usou o recurso {low_priority_count} vezes.")
print("------------------------")