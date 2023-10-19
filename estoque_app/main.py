from models import Produto, Lote
from database import csv_handler
from utils import produtos_em_poder_de_terceiros, produtos_de_terceiros_em_meu_poder



# criando novo produto
produto1 = Produto('1', 'Coca-Cola', 'Refrigerante de cola', '7894900011517', 'Bebidas', 5.00, 7.00)

# adicionando lotes ao produto
lote1 = Lote('1', produto1.id, '123456', 100, '2021-12-31', 'A1')
produto1.adicionar_lote(lote1)

# salvando produto no arquivo csv
csv_handler.salvar_produto_csv(produto1)

# ler produtos do arquivo csv
produtos = csv_handler.ler_produtos_csv()
for produto in produtos:
    print(produto.nome)
    print(produto.obter_quantidade_total())
    print(produto.lotes[0].numero_lote)
    print(produto.lotes[0].quantidade)
    print(produto.lotes[0].data_validade)
    print(produto.lotes[0].localizacao)
    print(produto.lotes[0].em_poder_de_terceiros)
    print(produto.lotes[0].data_criacao)
    print(produto.lotes[0].data_atualizacao)
    print(produto.lotes[0].data_exclusao)
    print('-----------------')

# produtos em poder de terceiros
produtos_em_poder_de_terceiros = produtos_em_poder_de_terceiros(produtos)
for produto in produtos_em_poder_de_terceiros:
    print(produto.nome)
    print(produto.obter_quantidade_total())
    print(produto.lotes[0].numero_lote)
    print(produto.lotes[0].quantidade)
    print(produto.lotes[0].data_validade)
    print(produto.lotes[0].localizacao)
    print(produto.lotes[0].em_poder_de_terceiros)
    print(produto.lotes[0].data_criacao)
    print(produto.lotes[0].data_atualizacao)
    print(produto.lotes[0].data_exclusao)
    print('-----------------')

# produtos de terceiros em meu poder
produtos_de_terceiros_em_meu_poder = produtos_de_terceiros_em_meu_poder(produtos)
for produto in produtos_de_terceiros_em_meu_poder:
    print(produto.nome)
    print(produto.obter_quantidade_total())
    print(produto.lotes[0].numero_lote)
    print(produto.lotes[0].quantidade)
    print(produto.lotes[0].data_validade)
    print(produto.lotes[0].localizacao)
    print(produto.lotes[0].em_poder_de_terceiros)
    print(produto.lotes[0].data_criacao)
    print(produto.lotes[0].data_atualizacao)
    print(produto.lotes[0].data_exclusao)
    print('-----------------')
    