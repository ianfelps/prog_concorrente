# Servidor - Fatorial

import socket

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
                    if data.decode().strip().lower() == "fatorial":
                        response = "numero"
                        conn.sendall(response.encode()) # Envia a resposta
                        # Receber o valor do fatorial
                        data = conn.recv(1024)
                        num = int(data.decode())
                        print(f"Calculando fatorial de {num} ...")
                        # Calcular o fatorial
                        result = 1
                        for i in range(1, num + 1):
                            result *= i
                        # Enviar o resultado
                        response = f"O fatorial de {num} é igual a: {result} !"
                        conn.sendall(response.encode())
                        print("Fatorial calculado!")
                    else:
                        conn.sendall(b"Comando desconhecido")

if __name__ == "__main__":
    start_server()