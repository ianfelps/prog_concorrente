import psutil

# Lista todos os processos ativos
for proc in psutil.process_iter(['pid', 'name', 'status']):
    try:
        # Verifica se o processo está em execução (running)
        if proc.info['status'] == psutil.STATUS_RUNNING:
            print(f"PID: {proc.info['pid']}, Nome: {proc.info['name']}, Estado: {proc.info['status']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Ignora exceções para processos problemáticos
        pass
