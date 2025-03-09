import threading
from time import sleep

lock1 = threading.Lock()
lock2 = threading.Lock()

def T1():
    print("T1: Tentando adquirir o lock1...")
    lock1.acquire()
    print("T1: lock1 adquirido! Tentando adquirir o lock2...")
    sleep(1)
    lock2.acquire()
    print("T1: lock2 adquirido!")
    lock2.release()
    lock1.release()
    print("T1: Finalizada!")

def T2():
    print("T2: Tentando adquirir o lock2...")
    lock2.acquire()
    print("T2: lock2 adquirido! Tentando adquirir o lock1...")
    sleep(1)
    lock1.acquire()
    print("T2: lock1 adquirido!")
    lock1.release()
    lock2.release()
    print("T2: Finalizada!")

# Uso
t1 = threading.Thread(target=T1)
t2 = threading.Thread(target=T2)

t1.start()
t2.start()
t1.join()
t2.join()