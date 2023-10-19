import uuid # Biblioteca para gerar o id do lote
from datetime import datetime # Biblioteca para trabalhar com datas





# lote.py

class Lote:
    def __init__(self, id, produto_id, numero_lote=None, quantidade=None, data_validade=None, localizacao=None, em_poder_de_terceiros=False, data_criacao=None, data_atualizacao=None, data_exclusao=None):
        self.id = id
        self.produto_id = produto_id
        self.numero_lote = numero_lote
        self.quantidade = quantidade
        self.data_validade = data_validade
        self.localizacao = localizacao
        self.em_poder_de_terceiros = em_poder_de_terceiros
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_exclusao = data_exclusao

        
