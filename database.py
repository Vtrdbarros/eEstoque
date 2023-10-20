import Produto
import mysql.connector 
import logging
import tkinter as tk
from tkinter import simpledialog, messagebox

# Configurando o logging
logging.basicConfig(level=logging.INFO)

# Configurações do banco de dados
DB_CONFIG = {
    "host": "localhost", # 
    "user": "root",  # Atualize esta linha
    "password": "Tech#2023",  # Certifique-se de que esta é a senha correta para o usuário tech_integra
    "database": "estoque"
}

def get_connection():
    """Estabelece e retorna uma conexão com o banco de dados."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        logging.info("Conexão com o banco de dados estabelecida com sucesso!")
        return conn
    except mysql.connector.Error as err:
        logging.error(f"Erro ao conectar no banco de dados: {err}")
        return None
def close_connection(conn):
    """Fecha a conexão com o banco de dados."""
    if conn:
        conn.close()
        logging.info("Conexão com o banco de dados fechada com sucesso!")

def inserir_produto(produto):
    """Insere um produto no banco de dados."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO produtos (nome, descricao, codigo_barras, categoria, preco_compra, preco_venda) VALUES (%s, %s, %s, %s, %s, %s)
        """, (produto.nome, produto.descricao, produto.codigo_barras, produto.categoria, produto.preco_compra, produto.preco_venda))
        conn.commit()
    except mysql.connector.Error as err:
        logging.error(f"Erro ao inserir produto: {err}")
    finally:
        cursor.close()
        close_connection(conn)

def remover_produto(id):
    """Remove um produto pelo ID."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
        conn.commit()
    except mysql.connector.Error as err:
        logging.error(f"Erro ao remover produto: {err}")
    finally:
        cursor.close()
        close_connection(conn)

def listar_produtos():
    """Lista todos os produtos."""
    conn = get_connection()
    cursor = conn.cursor()
    produtos = []
    try:
        cursor.execute("SELECT * FROM produtos")
        for produto in cursor.fetchall():
            produtos.append(produto)
    except mysql.connector.Error as err:
        logging.error(f"Erro ao listar produtos: {err}")
    finally:
        cursor.close()
        close_connection(conn)
    return produtos

def atualizar_produto(produto):
    """Atualiza um produto existente."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE produtos SET nome = %s, descricao = %s, codigo_barras = %s, categoria = %s, preco_compra = %s, preco_venda = %s WHERE id = %s
        """, (produto.nome, produto.descricao, produto.codigo_barras, produto.categoria, produto.preco_compra, produto.preco_venda, produto.id))
        conn.commit()
    except mysql.connector.Error as err:
        logging.error(f"Erro ao atualizar produto: {err}")
    finally:
        cursor.close()
        close_connection(conn)

def test_connection():
    """Testa a conexão com o banco de dados."""
    conn = get_connection()
    if conn:
        print("Conexão com o banco de dados estabelecida com sucesso!")
        close_connection(conn)
    else:
        print("Falha ao conectar ao banco de dados.")

if __name__ == "__main__":
    test_connection()

def on_add_product():
    """Função chamada quando o botão 'Adicionar Produto' é pressionado."""
    nome = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:")
    descricao = simpledialog.askstring("Adicionar Produto", "Digite a descrição do produto:")
    codigo_barras = simpledialog.askstring("Adicionar Produto", "Digite o código de barras do produto:")
    categoria = simpledialog.askstring("Adicionar Produto", "Digite a categoria do produto:")
    preco_compra = simpledialog.askfloat("Adicionar Produto", "Digite o preço de compra do produto:")
    preco_venda = simpledialog.askfloat("Adicionar Produto", "Digite o preço de venda do produto:")

    produto = Produto(None, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda)
    inserir_produto(produto)
    messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

def on_remove_product():
    """Função chamada quando o botão 'Remover Produto' é pressionado."""
    id = simpledialog.askinteger("Remover Produto", "Digite o ID do produto a ser removido:")
    remover_produto(id)
    messagebox.showinfo("Sucesso", f"Produto com ID {id} removido com sucesso!")

def on_list_products():
    """Função chamada quando o botão 'Listar Produtos' é pressionado."""
    produtos = listar_produtos()
    output = ""
    for produto in produtos:
        output += f"ID: {produto[0]}, Nome: {produto[1]}, Descrição: {produto[2]}, Código de Barras: {produto[3]}, Categoria: {produto[4]}, Preço de Compra: {produto[5]}, Preço de Venda: {produto[6]}\n"
    messagebox.showinfo("Produtos", output)

# Criando a janela principal
root = tk.Tk()
root.title("Gerenciamento de Produtos")

# Adicionando botões
btn_add = tk.Button(root, text="Adicionar Produto", command=on_add_product)
btn_add.pack(pady=20)

btn_remove = tk.Button(root, text="Remover Produto", command=on_remove_product)
btn_remove.pack(pady=20)

btn_list = tk.Button(root, text="Listar Produtos", command=on_list_products)
btn_list.pack(pady=20)

root.mainloop()
