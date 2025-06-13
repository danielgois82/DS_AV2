import requests
import pandas as pd

def requestAPIBCB(data: int) -> pd.DataFrame:
    """
    Requisicao da API do BCB sobre dados publicos referente a Execução Orçamentária por Pares Código-Conta por ano \n
    Parametro: Data - Inteiro, formato AAAA, ex: 2024 \n
    Saida: Um Pandas DataFrame
    """

    url = f"https://olinda.bcb.gov.br/olinda/servico/SIORC/versao/v1/odata/RelatorioParOAMPorAno(Ano=@Ano)?@Ano={data}&$format=json"

    req = requests.get(url)
    print("Status code:", req.status_code)
    dados = req.json()
    df = pd.json_normalize(dados["value"])
    return df