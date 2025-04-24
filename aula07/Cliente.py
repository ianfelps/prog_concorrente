import requests

BASE_URL = 'http://127.0.0.1:5000'

# Função para listar produtos
def listar_produtos():
    response = requests.get(f'{BASE_URL}/produtos')
    if response.status_code == 200:
        print("Lista de Produtos:")
        for produto in response.json():
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}")
    else:
        print("Erro ao listar produtos.")

# Função para adicionar um produto
def adicionar_produto(nome, preco):
    novo_produto = {'nome': nome, 'preco': preco}
    response = requests.post(f'{BASE_URL}/produtos', json=novo_produto)
    if response.status_code == 201:
        print("Produto adicionado com sucesso!")
    else:
        print("Erro ao adicionar produto:", response.json())

# Função para buscar um produto pelo ID
def buscar_produto(id):
    response = requests.get(f'{BASE_URL}/produtos/{id}')
    if response.status_code == 200:
        print("Produto Encontrado:")
        produto = response.json()
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}")
    else:
        print("Erro ao buscar produto:", response.json())

# Menu interativo
def menu():
    while True:
        print("\nMenu:")
        print("1 - Listar Produtos")
        print("2 - Adicionar Produto")
        print("3 - Buscar Produto por ID")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_produtos()
        elif opcao == '2':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            adicionar_produto(nome, preco)
        elif opcao == '3':
            id = input("ID do produto: ")
            buscar_produto(id)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()