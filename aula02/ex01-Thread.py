import threading
import time

def saudacao(nome, tempo):
    print(f"Olá, {nome}")
    time.sleep(tempo)
    print(f"Tchau, {nome}")

threadA = threading.Thread(target = saudacao, args = ("Ana", 5))
threadB = threading.Thread(target = saudacao, args = ("Beatriz", 2))

threadA.start()
threadB.start()
threadA.join()
threadB.join()

print("Thread principal finalizada")