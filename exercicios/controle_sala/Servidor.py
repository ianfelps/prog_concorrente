import socket
import threading

CAPACIDADE_SALA = 5
semaforo_sala = threading.Semaphore(CAPACIDADE_SALA)

ocupantes = []

def lidar_com_cliente(conn, addr):
    print(f"[+] Conexão estabelecida com {addr}")

    try:
        while True:
            mensagem = conn.recv(1024).decode()

            if not mensagem:
                break

            if mensagem == "ENTRAR":
                if semaforo_sala.acquire(blocking=False):
                    ocupantes.append(addr)
                    print(f"[ENTROU] {addr} | Total na sala: {len(ocupantes)}/{CAPACIDADE_SALA}")
                    conn.send(f"ENTRADA_PERMITIDA|{len(ocupantes)}/{CAPACIDADE_SALA}".encode())
                else:
                    print(f"[BLOQUEADO] {addr} tentou entrar | Sala cheia ({len(ocupantes)}/{CAPACIDADE_SALA})")
                    conn.send(f"SALA_CHEIA|{len(ocupantes)}/{CAPACIDADE_SALA}".encode())

            elif mensagem == "SAIR":
                if addr in ocupantes:
                    ocupantes.remove(addr)
                    semaforo_sala.release()
                    print(f"[SAIU] {addr} | Total na sala: {len(ocupantes)}/{CAPACIDADE_SALA}")
                    conn.send(f"SAIDA_CONFIRMADA|{len(ocupantes)}/{CAPACIDADE_SALA}".encode())
                else:
                    print(f"[FALHA] {addr} tentou sair | Não estava na sala")
                    conn.send("NAO_ESTA_NA_SALA".encode())

            else:
                print(f"[ERRO] {addr} enviou comando inválido: {mensagem}")
                conn.send("COMANDO_INVALIDO".encode())

    except Exception as e:
        print(f"[ERRO] Problema com {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Conexão encerrada com {addr}")

def iniciar_servidor():
    HOST = 'localhost'
    PORT = 12345

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"[SERVIDOR] Em execução em {HOST}:{PORT}")

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
