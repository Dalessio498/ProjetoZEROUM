import pyautogui as pg
import time
import pandas as pd



# URL da página
url = "http://localhost:8080/produtos"

# --- ABRIR O CHROME ---
pg.press("win")
time.sleep(1)
pg.write("chrome")
time.sleep(1)
pg.press("enter")
time.sleep(2)

# Digitar URL
pg.write(url)
pg.press("enter")
time.sleep(3) 


tabela = pd.read_csv("produtos_variados.csv")


for linha in tabela.index:

    # Nome do produto
    pg.press("tab")
    nome = tabela.loc[linha, "nome_produto"]
    pg.write(str(nome))
    time.sleep(0.5)

    # Marca
    pg.press("tab")
    marca = tabela.loc[linha, "marca_produto"]
    pg.write(str(marca))
    time.sleep(0.5)

    # Categoria
    pg.press("tab")
    categoria = tabela.loc[linha, "categoria_produto"]
    pg.write(str(categoria))
    time.sleep(0.5)

    # Preço
    pg.press("tab")
    preco = str(tabela.loc[linha, "preco_produto"])
    pg.write(preco)
    time.sleep(0.5)

    pg.press("enter")
    time.sleep(1)  
