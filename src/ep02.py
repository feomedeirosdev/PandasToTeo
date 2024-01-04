import pandas as pd
import os 
import ast

# generalizando caminhos dos arquivos para qualquer sistema operacional
endereco_programa = os.path.join(os.path.abspath('.'), 'src')
endereco_programa = os.path.dirname(os.path.abspath(__file__)) 
endereco_projeto = os.path.dirname(endereco_programa)
endereco_dados = os.path.join(endereco_projeto, 'data')

# Início
filepath_candidatura_csv = os.path.join(endereco_dados, 'tb_candidatura_2018.csv')
df_candidatura = pd.read_csv(filepath_candidatura_csv, sep = ';')

df_candidatura.head()

##################################
# Combinando e modificando colunas
##################################

print(df_candidatura.columns)

print(df_candidatura[['idade_data_eleicao', 'idade_data_posse']])
print(df_candidatura[['idade_data_eleicao', 'idade_data_posse']].info())
print(df_candidatura[['idade_data_eleicao', 'idade_data_posse']].dtypes)
print(type(df_candidatura[['idade_data_eleicao', 'idade_data_posse']].dtypes))
print(type(df_candidatura[['idade_data_eleicao', 'idade_data_posse']].dtypes[0]))

# df_candidatura[['idade_eleicao', 'idade_posse']] = df_candidatura[['idade_data_eleicao', 'idade_data_posse']].astype(int)

idades_antigas = ['idade_data_eleicao', 'idade_data_posse']
idades_novas = ['idade_eleicao', 'idade_posse']

# Descreve estatísticas da coluna ou do DataFrame
print(df_candidatura[idades_antigas].describe())

# # Deletando coluna
# del df_candidatura['idade_data_eleicao']
print(df_candidatura)

# Deletando coluna com dado faltante
df_candidatura_novo = df_candidatura.dropna(how='all', axis=1).copy() # Retorna um DataFrame novo
print(df_candidatura_novo)
print(df_candidatura)

# Deletando linha com dados faltantes
# df_candidatura.dropna(subset=['cpf'], how='all', axis=0)
df_candidatura_novo['idade_data_posse']

print(df_candidatura.columns)
print(df_candidatura_novo.columns)

df_candidatura_novo['idade_data_posse'].astype(int)
