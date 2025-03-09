import threading
from time import sleep

# Definir o contador
Contador = 0
lock = threading.Lock()

def incrementar():
    global Contador
    for _ in range(1000):
        lock.acquire() # Adquire o lock antes de incrementar
        try:
            Contador += 1
        finally:
            lock.release() # Libera o lock depois de incrementar

threads = []

for i in range(10):
    thread = threading.Thread(target=incrementar)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Contador final: {Contador}")