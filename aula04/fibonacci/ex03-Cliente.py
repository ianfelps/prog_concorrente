# Cliente

import socket

def start_client():

    # Configurações do servidor
    HOST = '127.0.0.1' # Endereco IP
    PORT = 65432 # Porta

    # Conexão socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.connect((HOST, PORT)) # Conectar ao servidor
        print(f"Conectado ao servidor em {HOST}:{PORT} ! Solicitando data e hora ...")
        # Enviar solicitação
        S.sendall(b"fibonacci")
        # Receber resposta
        data = S.recv(1024)
        # Verificar o comando
        if data.decode() == "numero":
            # Imprimir resposta
            print("Insira um número para descobrir sua posição na sequência de fibonacci: ")
            # Enviar solicitação
            num = input(">>> ")
            S.sendall(num.encode())
            # Receber resposta
            result = S.recv(1024)
            # Imprimir resposta
            print(f"Resposta do servidor: {result.decode()}")

if __name__ == "__main__":
    start_client()