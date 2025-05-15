# Servidor - Data e Hora

import socket
from datetime import datetime

def start_server():

    # Configurações do servidor
    HOST = '127.0.0.1' # Endereco IP
    PORT = 65432 # Porta

    # Conexão socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.bind((HOST, PORT)) # Vincular endereço e porta
        S.listen() # Escutar conexões
        print(f"Servidor ouvindo em {HOST}:{PORT} ...")
        # Aceitar conexões
        while True:
            conn, addr = S.accept()
            with conn:
                print(f"Conectado por {addr} !")
                # Receber dados
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    # Verificar o comando
                    if data.decode().strip().lower() == "data e hora":
                        # Obtem e formata a data e a hora
                        now = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
                        response = f"Data e Hora Atual: {now}"
                        conn.sendall(response.encode()) # Envia a resposta
                    else:
                        conn.sendall(b"Comando desconhecido")

if __name__ == "__main__":
    start_server()