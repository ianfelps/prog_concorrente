import psutil

# Obter memória de um processo
def obter_memoria_processo(pid):
    try:
        # Obter informações do processo
        processo = psutil.Process(pid)
        memoria_info = processo.memory_info()
        # Converter para MB
        memoria_fisica_mb = memoria_info.rss / (1024 * 1024) # Resident Set Size
        memoria_virtual_mb = memoria_info.vms / (1024 * 1024) # Virtual Memory Size
        return memoria_fisica_mb, memoria_virtual_mb
    except psutil.NoSuchProcess:
        return None, None

# Uso
pid = 0
memoria_fisica, memoria_virtual = obter_memoria_processo(pid)

if memoria_fisica is not None:
    print(f"Processo PID {pid}:")
    print(f"Memória Física (RSS): {memoria_fisica:.2f} MB")
    print(f"Memória Virtual (VMS): {memoria_virtual:.2f} MB")
else:
    print(f"Processo com PID {pid} não encontrado.")
