
import mysql.connector 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Configuração do banco e query
db_config = {
    'host': 'localhost', 
    'user': 'root', 
    'password': 'Mad@20200', 
    'database': 'teste' 
}
query = "select * from produto"

# Função para conectar, buscar dados e fechar conexão
def inicio_conexao():
    try:
        conexao = mysql.connector.connect(**db_config)
        print("Conexão bem-sucedida!")
        
        df = pd.read_sql_query(query, conexao)
        print(f"Dados extraídos: {len(df)} linhas.")
        return df
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
            print("Conexão com o MySQL fechada.")

df = inicio_conexao()  # Obtém os dados

print(df, "\n")

# Soma do valor vendido por categoria
ValorVendidoPorCategoria = df.groupby('categoria_produto')['preco_produto'].sum().reset_index()
ValorVendidoPorCategoria = ValorVendidoPorCategoria.rename(columns={'categoria_produto': "Categoria", 'preco_produto': "Valor total"})
print(ValorVendidoPorCategoria, "\n")

# Quantidade de itens por categoria
QuantidadeCategoria = df.groupby('categoria_produto').size().reset_index(name="QTD itens")
QuantidadeCategoria = QuantidadeCategoria.rename(columns={'categoria_produto': 'Categoria'})
print(QuantidadeCategoria, "\n")

# Produto mais caro
produto_mais_caro = df.loc[df['preco_produto'].idxmax()]
print("Produto mais caro:")
print(produto_mais_caro, "\n")

# Produto mais barato
produto_mais_barato = df.loc[df['preco_produto'].idxmin()]
print("Produto mais barato:")
print(produto_mais_barato, "\n")

# Paleta de cores para os gráficos
cores1 = [ 
    "#e84b2c", "#e8c62c", "#e5e82c", "#87e82c", "#ad2ce8", "#482ce8", "#2cb3e8", "#2ce86b"
]

# Gráfico: valor arrecadado por categoria
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x='categoria_produto',
    y='preco_produto',
    linewidth=2.5,
    palette=cores1,
    errorbar=None
)
plt.title('Arrecadado por categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor arrecadado')
plt.show()

# Gráfico: quantidade de itens por categoria
plt.figure(figsize=(10,6))
sns.barplot(
    data=QuantidadeCategoria,
    y='Categoria',
    x='QTD itens',
    linewidth=2.5,
    palette=cores1,
    errorbar=None
)
plt.title('Quantidade por categoria')
plt.ylabel('Categoria')
plt.xlabel('Quantidade de itens')
plt.show()
