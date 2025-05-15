# Servidor - Fatorial

import socket

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

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
                    if data.decode().strip().lower() == "fibonacci":
                        response = "numero"
                        conn.sendall(response.encode()) # Envia a resposta
                        # Receber o valor da posição
                        data = conn.recv(1024)
                        num = int(data.decode())
                        print(f"Calculando a posição de {num} na sequencia de Fibonacci ...")
                        # Calcular fibonacci
                        result = fibonacci(num)
                        # Enviar o resultado
                        response = f"A posição {num} na sequência de Fibonacci é igual a: {result} !"
                        conn.sendall(response.encode())
                        print("Fibonacci calculado!")
                    else:
                        conn.sendall(b"Comando desconhecido")

if __name__ == "__main__":
    start_server()