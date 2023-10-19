import csv



# Path: estoque_app/database/csv_handler.py

# função para salvar um produto no arquivo csv
def salvar_produto_csv(produto, arquivo='produtos.csv'):
    print(f"Salvando produto {produto.nome} no arquivo {arquivo}")
    with open(arquivo, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([produto.id, produto.nome, produto.descricao, produto.codigo_barras, produto.categoria, produto.preco_compra, produto.preco_venda])
    print(f"Produto {produto.nome} salvo no arquivo {arquivo}")

# função para salvar um lote no arquivo csv
def salvar_lote_csv(lote, arquivo='lotes.csv'):
    print(f"Salvando lote {lote.numero_lote} no arquivo {arquivo}")
    with open(arquivo, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lote.id, lote.produto_id, lote.numero_lote, lote.quantidade, lote.data_validade, lote.localizacao, lote.em_poder_de_terceiros])
    print(f"Lote {lote.numero_lote} salvo no arquivo {arquivo}")

# Função para remover um produto do arquivo CSV
def remover_produto_csv(id, arquivo='produtos.csv'):
    print(f"Removendo produto {id} do arquivo {arquivo}")
    produtos = ler_produtos_csv(arquivo)
    with open(arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        for produto in produtos:
            if produto.id != id:
                writer.writerow([produto.id, produto.nome, produto.descricao, produto.codigo_barras, produto.categoria, produto.preco_compra, produto.preco_venda])
    print(f"Produto {id} removido do arquivo {arquivo}")

# função para atualizar um produto no arquivo csv
def atualizar_produto_csv(id, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda, arquivo='produtos.csv'):
    print(f"Atualizando produto {id} no arquivo {arquivo}")
    produtos = ler_produtos_csv(arquivo)
    with open(arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        for produto in produtos:
            if produto.id == id:
                produto.nome = nome
                produto.descricao = descricao
                produto.codigo_barras = codigo_barras
                produto.categoria = categoria
                produto.preco_compra = preco_compra
                produto.preco_venda = preco_venda
            writer.writerow([produto.id, produto.nome, produto.descricao, produto.codigo_barras, produto.categoria, produto.preco_compra, produto.preco_venda])
    print(f"Produto {id} atualizado no arquivo {arquivo}")

# função para remover um lote do arquivo csv
def remover_lote_csv(id, arquivo='lotes.csv'):
    print(f"Removendo lote {id} do arquivo {arquivo}")
    lotes = ler_lotes_csv(arquivo)
    with open(arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        for lote in lotes:
            if lote.id != id:
                writer.writerow([lote.id, lote.produto_id, lote.numero_lote, lote.quantidade, lote.data_validade, lote.localizacao, lote.em_poder_de_terceiros])
    print(f"Lote {id} removido do arquivo {arquivo}")

# função para atualizar um lote no arquivo csv
def atualizar_lote_csv(id, produto_id, numero_lote, quantidade, data_validade, localizacao, em_poder_de_terceiros=False, arquivo='lotes.csv'):
    print(f"função para atualizar um lote no arquivo csv {id} do arquivo {arquivo}")
    lotes = ler_lotes_csv(arquivo)
    with open(arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        for lote in lotes:
            if lote.id == id:
                lote.produto_id = produto_id
                lote.numero_lote = numero_lote
                lote.quantidade = quantidade
                lote.data_validade = data_validade
                lote.localizacao = localizacao
                lote.em_poder_de_terceiros = em_poder_de_terceiros
            writer.writerow([lote.id, lote.produto_id, lote.numero_lote, lote.quantidade, lote.data_validade, lote.localizacao, lote.em_poder_de_terceiros])

# função para ler os produtos do arquivo csv
def ler_produtos_csv(arquivo='produtos.csv'):
    print(f"Função para ler os produtos do arquivo CSV {arquivo}")
    produtos = []
    try:
        with open(arquivo, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                produto = Produto(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                produtos.append(produto)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado. Criando um novo arquivo.")
        with open(arquivo, 'w', newline='') as file:
            pass
    return produtos

# função para ler os lotes do arquivo csv
def ler_lotes_csv(arquivo='lotes.csv'):
    print(f"Função para ler os lotes do arquivo CSV {arquivo}")
    lotes = []
    with open(arquivo, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            lote = Lote(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            lotes.append(lote)
    return lotes
# função para obter um produto do arquivo csv
def obter_produto_csv(id, arquivo='produtos.csv'):
    print(f"função para obter um produto do arquivo csv {id} do arquivo {arquivo}")
    produtos = ler_produtos_csv(arquivo)
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

# função para obter um lote do arquivo csv
def obter_lote_csv(id, arquivo='lotes.csv'):
    print(f"Função para obter um lote do arquivo csv {id} do arquivo {arquivo}")
    lotes = ler_lotes_csv(arquivo)
    for lote in lotes:
        if lote.id == id:
            return lote
    return None

# função para obter os produtos em poder de terceiros do arquivo csv
def obter_produtos_em_poder_de_terceiros_csv(arquivo='produtos.csv'):
    print(f"Função para obter os produtos em poder de terceiros do arquivo CSV {arquivo}")
    produtos = ler_produtos_csv(arquivo)
    produtos_em_poder_de_terceiros = []
    for produto in produtos:
        if produto.obter_quantidade_total() > 0:
            produtos_em_poder_de_terceiros.append(produto)
    return produtos_em_poder_de_terceiros

# função para obter os produtos de terceiros em meu poder do arquivo csv
def obter_produtos_de_terceiros_em_meu_poder_csv(arquivo='produtos.csv'):
    print(f"Função para obter os produtos de terceiros em meu poder do arquivo CSV {arquivo}")
    produtos = ler_produtos_csv(arquivo)
    produtos_de_terceiros_em_meu_poder = []
    for produto in produtos:
        if produto.obter_quantidade_total() > 0:
            produtos_de_terceiros_em_meu_poder.append(produto)
    return produtos_de_terceiros_em_meu_poder

# função para obter os lotes em poder de terceiros do arquivo csv
def obter_lotes_em_poder_de_terceiros_csv(arquivo='lotes.csv'):
    print(f"Função para obter os lotes em poder de terceiros do arquivo CSV {arquivo}")
    lotes = ler_lotes_csv(arquivo)
    lotes_em_poder_de_terceiros = []
    for lote in lotes:
        if lote.em_poder_de_terceiros:
            lotes_em_poder_de_terceiros.append(lote)
    return lotes_em_poder_de_terceiros

# função para obter os lotes de terceiros em meu poder do arquivo csv
def obter_lotes_de_terceiros_em_meu_poder_csv(arquivo='lotes.csv'):
    print(f"Função para obter os lotes de terceiros em meu poder do arquivo CSV {arquivo}")
    lotes = ler_lotes_csv(arquivo)
    lotes_de_terceiros_em_meu_poder = []
    for lote in lotes:
        if not lote.em_poder_de_terceiros:
            lotes_de_terceiros_em_meu_poder.append(lote)
    return lotes_de_terceiros_em_meu_poder

# função para obter os lotes por produto do arquivo csv
def obter_lotes_por_produto_csv(produto_id, arquivo='lotes.csv'):
    print(f"Função para obter os lotes por produto do arquivo CSV {arquivo} para o produto {produto_id}")
    lotes = ler_lotes_csv(arquivo)
    lotes_por_produto = []
    for lote in lotes:
        if lote.produto_id == produto_id:
            lotes_por_produto.append(lote)
    return lotes_por_produto

