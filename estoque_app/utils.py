




def filtrar_produtos_por_condicao(produtos, condicao):
    produtos_filtrados = set()
    for produto in produtos:
        for lote in produto.lotes:
            if condicao(lote):
                produtos_filtrados.add(produto)
    return list(produtos_filtrados)

def produtos_em_poder_de_terceiros(produtos):
    return filtrar_produtos_por_condicao(produtos, lambda lote: lote.em_poder_de_terceiros)

def produtos_de_terceiros_em_meu_poder(produtos):
    return filtrar_produtos_por_condicao(produtos, lambda lote: not lote.em_poder_de_terceiros)
