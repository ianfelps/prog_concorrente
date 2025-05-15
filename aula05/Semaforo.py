import threading

S = threading.Semaphore(3) # Semáforo com limite de 3 threads
X = 1
def acessoRecurso(thread_id):
    global X
    print(f"Thread {thread_id} tentando acessar o recurso...")
    with S:
        print(f"Thread {thread_id} acessou o recurso!")
        threading.Event().wait(1)
        X = X * 2
    print(f"Thread {thread_id} liberou o recurso!")

threads = [threading.Thread(target=acessoRecurso, args=(i,)) for i in range(5)]

for t in threads: t.start()
for t in threads: t.join()

print("Encerrando ...")
print(f"X = {X}")