from produto import Produto
from cs_handler import ler_produtos_csv





def menu():
    while True:
        print("\n--- Menu de Gerenciamento de Produtos ---")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            id = input("Digite o ID do produto: ")
            nome = input("Digite o nome do produto: ")
            descricao = input("Digite a descrição do produto: ")
            codigo_barras = input("Digite o código de barras do produto: ")
            categoria = input("Digite a categoria do produto: ")
            preco_compra = float(input("Digite o preço de compra do produto: "))
            preco_venda = float(input("Digite o preço de venda do produto: "))
            
            produto = Produto(id, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda)
            # salvando produto no arquivo csv
            salvar_produto_csv(produto)
            
            
            print(f"Produto {nome} adicionado com sucesso!")
        
        elif opcao == "2":
            id = input("Digite o ID do produto que deseja remover: ")
            # Aqui você pode chamar a função para remover o produto do CSV ou de qualquer outro local de armazenamento.
            
            print(f"Produto com ID {id} removido com sucesso!")
        
        elif opcao == "3":
            # Aqui você pode chamar a função para listar os produtos do CSV ou de qualquer outro local de armazenamento.
            produtos = ler_produtos_csv()
            for produto in produtos:
                print(produto.__dict__)
        
        elif opcao == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

menu()
