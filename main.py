import pandas as pd
from src.extractTransform import requestAPIBCB
from src.load import salvarSQLite, salvarCSV

ano = 2024

dados_bcb = requestAPIBCB(ano)

salvarCSV(dados_bcb, 'src/datasets/oam.csv', ';', '.')

salvarSQLite(dados_bcb, 'src/datasets/oam.db', 'oam')
