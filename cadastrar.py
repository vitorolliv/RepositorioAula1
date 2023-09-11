# Inicialize um dicionário vazio para armazenar os produtos
produtos = {}

# Função para cadastrar um novo produto
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos[nome] = {"preco": preco, "quantidade": quantidade}
    print(f"Produto {nome} cadastrado com sucesso!")

# Função para listar todos os produtos
def listar_produtos():
    print("Lista de Produtos:")
    for nome, info in produtos.items():
        print(f"Nome: {nome}, Preço: R${info['preco']}, Quantidade em Estoque: {info['quantidade']}")

# Função principal
def main():
    while True:
        print("\nOpções:")
        print("1. Cadastrar novo produto")
        print("2. Listar produtos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
