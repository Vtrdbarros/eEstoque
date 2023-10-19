from models import Produto, Lote
from database import csv_handler



def adicionar_produto(id, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda):
    produto = Produto(id, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda)
    csv_handler.salvar_produto_csv(produto)
    return produto

def adicionar_lote(id, produto_id, numero_lote, quantidade, data_validade, localizacao, em_poder_de_terceiros=False):
    lote = Lote(id, produto_id, numero_lote, quantidade, data_validade, localizacao, em_poder_de_terceiros)
    csv_handler.salvar_lote_csv(lote)
    return lote

def remover_produto(id):
    csv_handler.remover_produto_csv(id)
    pass

def atualizar_produto(id, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda):
    csv_handler.atualizar_produto_csv(id, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda)
    pass

def remover_lote(id):
    csv_handler.remover_lote_csv(id)
    pass

def atualizar_lote(id, produto_id, numero_lote, quantidade, data_validade, localizacao, em_poder_de_terceiros=False):
    csv_handler.atualizar_lote_csv(id, produto_id, numero_lote, quantidade, data_validade, localizacao, em_poder_de_terceiros)
    pass

def obter_produto(id):
    return csv_handler.obter_produto_csv(id)

def ober_produto_por_id(id):
    produto = obter_produtos()
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

def obter_lote_por_id(id):
    lote = obter_lotes()
    for lote in lotes:
        if lote.id == id:
            return lote
    return None
