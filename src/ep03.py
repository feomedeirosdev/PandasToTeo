import pandas as pd
import numpy as np
import os

# Generalizando caminho de arquivos para qualquer sistema operacional
path_prog = os.path.join(os.path.abspath('.'), 'scr')
path_prog = os.path.dirname(os.path.abspath(__file__))
path_proj = os.path.dirname(path_prog)
path_data = os.path.join(path_proj, 'data')

# print(path_prog)
# print(path_proj)
# print(path_data)

filepath_csv = '/home/medeiros/Documentos/PandasToTeo/data/tb_candidatura_2018.csv'
df_candidatura = pd.read_csv(filepath_csv, sep=';')

print(df_candidatura)

### Epsódio 03 - Limpando e filtrando dados
