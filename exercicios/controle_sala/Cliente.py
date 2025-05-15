import socket

def cliente():
    HOST = 'localhost'
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[CLIENTE] Conectado ao servidor.")

        while True:
            print("\n--- MENU ---")
            print("1. Entrar na sala")
            print("2. Sair da sala")
            print("3. Sair do programa")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                s.send("ENTRAR".encode())
                resposta = s.recv(1024).decode()
                partes = resposta.split("|")
                status = partes[0]
                ocupacao = partes[1] if len(partes) > 1 else "?"

                if status == "ENTRADA_PERMITIDA":
                    print(f"Você entrou na sala. Ocupantes: {ocupacao}")
                elif status == "SALA_CHEIA":
                    print(f"Sala cheia. Ocupantes: {ocupacao}")
                else:
                    print(f"Resposta do servidor: {resposta}")

            elif opcao == '2':
                s.send("SAIR".encode())
                resposta = s.recv(1024).decode()
                partes = resposta.split("|")
                status = partes[0]
                ocupacao = partes[1] if len(partes) > 1 else "?"

                if status == "SAIDA_CONFIRMADA":
                    print(f"Você saiu da sala. Ocupantes: {ocupacao}")
                elif status == "NAO_ESTA_NA_SALA":
                    print("Você não está na sala.")
                else:
                    print(f"Resposta do servidor: {resposta}")

            elif opcao == '3':
                print("Encerrando conexão...")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    cliente()
