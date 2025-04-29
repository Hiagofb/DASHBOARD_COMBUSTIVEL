import os
import pandas as pd
import chardet

caminho = r"C:\Users\hiago\OneDrive\Documentos\CURSOS\PORTIFOLIO\DASHBOARD_PRECO_COMBUSTIVEL"
lista_arquivos = os.listdir(f"{caminho}/DADOS")

colunas_necess = [
    "Regiao - Sigla",
    "Estado - Sigla",
    "Municipio",
    "Revenda",
    "Produto",
    "Data da Coleta",
    "Valor de Venda",
    "Unidade de Medida",
    "Bandeira",
]

df_final = pd.DataFrame()

for arquivo in lista_arquivos:
    caminho_arquivo = f"{caminho}/DADOS/{arquivo}"
    # Detecta o encoding
    with open(caminho_arquivo, 'rb') as f:
        resultado = chardet.detect(f.read(10000))

    df = pd.read_csv(caminho_arquivo, sep=';', encoding=resultado['encoding'])
    
    for coluna in df.columns:
        if coluna not in colunas_necess:
            df.drop(coluna, axis=1, inplace=True)

    df_final = pd.concat([df_final, df], ignore_index=True)
    
for coluna in df_final.columns:
    if coluna != "Valor de Venda":
        df_final[coluna] = df_final[coluna].astype("category")

