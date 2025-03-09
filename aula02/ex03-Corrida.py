import threading
from time import sleep

# Definir o contador
Contador = 0

def incrementar():
    global Contador
    for _ in range(5000):
        V = Contador
        sleep(0.001)
        Contador = V + 1

threads = []

for i in range(50):
    thread = threading.Thread(target=incrementar)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Contador final: {Contador}")