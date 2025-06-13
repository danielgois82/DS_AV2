import pandas as pd
import sqlite3

def salvarCSV(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Salvar em disco um arquivo .CSV a partir de um DataFrame \n
    Parametros: Um DataFrame, \n
    nome_arquivo: string - Caminho e nome do arquivo .CSV a ser criado, \n
    separador: string - Separador de dados do arquivo .CSV, ex.:  ";" ou ",", \n
    decimal: string - Separador de casas decimais, ex.: "." ou ",".
    """
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal, index=False)

def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):

    """
    Salvar em disco um arquivo .db a partir de um DataFrame \n
    Parametros:  \n
    Um DataFrame, \n
    nome_banco: string - Caminho e nome do arquivo .db a ser criado, \n
    nome_tabela: string - Nome da tabela que será criada no banco.
    """

    conn = sqlite3.connect(nome_banco)
    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)
    conn.close()
