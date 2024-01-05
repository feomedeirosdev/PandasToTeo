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

# Removendo colunas com todos os dados faltantes e linhas que tenham o campo 'cpf' nulos ('missins', 'None', 'NA' ou 'NaN')
df_candidatura_nova = df_candidatura.dropna(axis=1, how='all').dropna(axis=0, how='any', subset=['cpf']).copy()
print(df_candidatura_nova)

# Removendo linhas que não tem CPF
df_candidatura_nova = df_candidatura

# Exibindo registros nulos do DataFrame
print(df_candidatura.isna())
print()
print(df_candidatura_nova.isna())

# Somando e exibindo dados faltantes
print(df_candidatura.isna().sum())
print(type(df_candidatura.isna().sum()))

print(df_candidatura.iloc[3769:3801])

# Exibindo dados faltantes em %
print((df_candidatura.isna().sum() / df_candidatura.shape[0])*100)

# Quai os candidados a presidência da república?
print(df_candidatura['descricao_cargo'] == 'PRESIDENTE')

df_presidente = df_candidatura[(df_candidatura['descricao_cargo'] == 'PRESIDENTE')].copy()

# Mais de um filtro
# df_presidente = df_candidatura[(df_candidatura['descricao_cargo'] == 'PRESIDENTE') &
#                                (df_candidatura['sigla_partido'] == 'PT')]

print(df_presidente[['nome', 'sigla_partido']])

colunas_de_interesse = ['ano_eleicao',
                       'numero_turno',
                       'cpf',
                       'data_nascimento',
                       'descricao_cor_raca',
                       'descricao_estado_civil',
                       'descricao_genero',
                       'descricao_grau_instrucao',
                       'descricao_ocupacao',
                       'email',
                       'nome',
                       'nome_social',
                       'sigla_uf_nascimento',
                       'nome_partido',
                       'sigla_partido',
                       'descricao_cargo',
                       'nome_partido',
                       'sigla_partido',
                       'descricao_cargo',
                       'descricao_situacao_candidatura']

df_presidente = df_presidente[colunas_de_interesse]
print(df_presidente)
print(df_presidente['cpf'].nunique())

# Removendo duplicatas (usando 'cpf')
df_presidente = (df_presidente
                 .sort_values(by=['numero_turno'])
                 .drop_duplicates(subset=['cpf'], keep='first'))

df_presidente = df_presidente.where(df_presidente['descricao_situacao_candidatura'] == 'APTO').dropna(how='all')  # Faz o mesmo que a linha de baixo
df_presidente = df_presidente[df_presidente['descricao_situacao_candidatura'] == 'APTO'].copy() # Faz o mesmo que a linha de cima

df_presidente[['nome', 'descricao_cor_raca']]