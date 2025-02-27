import psutil

# Verifica o estado do processo
def estado_processo(pid):
    try:
        processo = psutil.Process(pid)
        estado = processo.status()
        return estado
    except psutil.NoSuchProcess:
        return "Processo não encontrado"

# Uso
pid = int(input("Digite o PID do processo: "))
estado = estado_processo(pid)
print(f"O estado do processo com PID {pid} é: {estado}")
