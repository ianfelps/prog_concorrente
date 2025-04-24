import socket
import threading

# Função para o peer agir como servidor
def iniciar_servidor(endereco, porta, arquivo):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((endereco, porta))
        servidor.listen()
        print(f"Peer aguardando conexões em {endereco}:{porta}...")

        while True:
            conexao, endereco_cliente = servidor.accept()
            print(f"Conexão recebida de {endereco_cliente}")

            try:
                # Enviar o arquivo solicitado
                with open(arquivo, 'rb') as f:
                    print(f"Enviando arquivo: {arquivo}")
                    while True:
                        dados = f.read(1024)
                        if not dados:
                            break
                        conexao.sendall(dados)
                print("Arquivo enviado com sucesso.")
            except FileNotFoundError:
                print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
            finally:
                conexao.close()

# Função para o peer agir como cliente
def baixar_arquivo(endereco, porta, nome_arquivo_saida):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((endereco, porta))
        print(f"Conectado ao peer em {endereco}:{porta}")

        # Receber o arquivo
        with open(nome_arquivo_saida, 'wb') as f:
            print(f"Recebendo arquivo e salvando como: {nome_arquivo_saida}")
            while True:
                dados = cliente.recv(1024)
                if not dados:
                    break
                f.write(dados)
        print("Arquivo recebido com sucesso.")

if __name__ == "__main__":
    # Configurações do peer
    ENDERECO = "127.0.0.1"  # Endereço local
    PORTA = 5100           # Porta do servidor deste peer
    ARQUIVO_PARA_COMPARTILHAR = "produtos.csv"  # Arquivo que este peer compartilha

    # Iniciar o servidor em uma thread separada
    thread_servidor = threading.Thread(target=iniciar_servidor, args=(ENDERECO, PORTA, ARQUIVO_PARA_COMPARTILHAR))
    thread_servidor.daemon = True  # A thread será encerrada quando o programa principal terminar
    thread_servidor.start()

    print(f"Peer iniciado. Servidor rodando em {ENDERECO}:{PORTA}.")

    # Loop para o peer agir como cliente
    while True:
        print("\nMenu:")
        print("1 - Baixar arquivo de outro peer")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            endereco_peer = input("Digite o endereço IP do peer remoto: ")
            porta_peer = int(input("Digite a porta do peer remoto: "))
            nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

            print(f"Tentando baixar arquivo de {endereco_peer}:{porta_peer}...")
            baixar_arquivo(endereco_peer, porta_peer, nome_arquivo_saida)
        elif opcao == "2":
            print("Encerrando peer...")
            break
        else:
            print("Opção inválida!")