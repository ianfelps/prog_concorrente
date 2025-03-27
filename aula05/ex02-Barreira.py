import threading

B = threading.Barrier(3)

def trabalho(thread_id):
    print(f"Thread {thread_id} iniciada!")
    threading.Event().wait(1)
    print(f"Thread {thread_id} chegou na barreira!")
    B.wait()
    print(f"Thread {thread_id} saiu da barreira!")

threads = [threading.Thread(target=trabalho, args=(i,)) for i in range(3)]

for t in threads: t.start()
for t in threads: t.join()

print("Encerrando ...")