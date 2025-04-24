from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
DATABASE = 'produtos.csv'

# Função para ler o arquivo CSV
def ler_produtos():
    if not os.path.exists(DATABASE):
        with open(DATABASE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nome', 'preco'])  # Cabeçalho
    with open(DATABASE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        produtos = list(reader)
    return produtos

# Função para salvar produtos no arquivo CSV
def salvar_produtos(produtos):
    with open(DATABASE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'nome', 'preco'])
        writer.writeheader()
        writer.writerows(produtos)

# Rota para listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = ler_produtos()
    return jsonify(produtos)

# Rota para adicionar um novo produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    novo_produto = request.json
    nome = novo_produto.get('nome')
    preco = novo_produto.get('preco')

    if not nome or not preco:
        return jsonify({'erro': 'Nome e preço são obrigatórios'}), 400

    produtos = ler_produtos()
    novo_id = str(int(produtos[-1]['id']) + 1) if produtos else '1'
    produtos.append({'id': novo_id, 'nome': nome, 'preco': str(preco)})
    salvar_produtos(produtos)

    return jsonify({'mensagem': 'Produto adicionado com sucesso', 'produto': {'id': novo_id, 'nome': nome, 'preco': str(preco)}}), 201

# Rota para buscar um produto pelo ID
@app.route('/produtos/<id>', methods=['GET'])
def buscar_produto(id):
    produtos = ler_produtos()
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        return jsonify(produto)
    return jsonify({'erro': 'Produto não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)