import time
import threading

# função para simular dispositivos de entrada e saída
def tarefa_io(id_tarefa):
    print(f"Tarefa {id_tarefa} iniciada!")
    time.sleep(2)
    print(f"Tarefa {id_tarefa} finalizada!")

# função de execução sequencial
def exe_sequencial():
    t0 = time.time()  # iniciar timer 
    for i in range(4):  # chamar a função 4x
        tarefa_io(i)
    tf = time.time()  # finaliza o timer
    tempo = tf - t0
    print(f"Tempo sequencial = {tempo:.4f} segundos")
    return tempo  # retornar o tempo para cálculo do speedup

# função de execução paralela
def exe_paralelizada():
    t0 = time.time()  # iniciar timer
    threads = []  # criar vetor de threads
    for i in range(4):  # criar 4 threads com a função
        thread = threading.Thread(target=tarefa_io, args=(i,))  # criar thread
        threads.append(thread)  # adicionar na lista
        thread.start()  # iniciar thread
    for thread in threads:  # esperar todas as threads terminarem
        thread.join()
    tf = time.time()  # finaliza o timer
    tempo = tf - t0
    print(f"Tempo paralelizado = {tempo:.4f} segundos")
    return tempo  # retornar o tempo para cálculo do speedup

# testes
print("===== Execução Sequencial =====")
tempo_sequencial = exe_sequencial()

print("===== Execução Paralelizada =====")
tempo_paralelizado = exe_paralelizada()

# cálculo do speedup
print("===== Speedup =====")
if tempo_paralelizado > 0:
    speedup = tempo_sequencial / tempo_paralelizado
    print(f"Speedup = {speedup:.4f}")
else:
    print("Não foi possível calcular o speedup.")