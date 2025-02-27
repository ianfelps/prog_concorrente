import psutil

# Obter e imprimir o consumo de memória (em MB) de um processo específico
def memoria_processo(pid):
    try:
        process = psutil.Process(pid)
        memory = process.memory_info()

        rss_memory = memory.rss / (1024 * 1024) # Memória Física
        vms_memory = memory.vms / (1024 * 1024) # Memoria Virtual

        print(f"Consumo de memória física: {rss_memory:.2f} MB")
        print(f"Consumo de memória virtual: {vms_memory:.2f} MB")
    except psutil.NoSuchProcess:
        print("Processo não encontrado!")

# Obter e imprimir status de um processo específico
def estado_processo(pid):
    try:
        process = psutil.Process(pid)
        status = process.status()
        print(f"Estado: {status}")
    except psutil.NoSuchProcess:
        print("Processo não encontrado!")

# Listar todos os processos em execução
def listar_processos():
    number_process = 0
    try:
        for process in psutil.process_iter(['pid', 'name', 'status']):
            if process.info['status'] == psutil.STATUS_RUNNING:
                print(f"PID: {process.info['pid']}, Nome: {process.info['name']}, Estado: {process.info['status']}")
                number_process += 1
        print(f"Número de processos: {number_process}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

pid = int(input("Digite o PID do processo: "))

memoria_processo(pid)
estado_processo(pid)

# listar_processos()