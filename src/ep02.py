import pandas as pd
import os 
import numpy as np

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
# print(df_candidatura)

# Deletando coluna com dado faltante
df_candidatura_novo = df_candidatura.dropna(how='all', axis=1).copy() # Retorna um DataFrame novo
print(df_candidatura_novo)
print(df_candidatura)

# Deletando linha com dados faltantes
# df_candidatura.dropna(subset=['cpf'], how='all', axis=0)
print(df_candidatura_novo['idade_data_posse'])

print(df_candidatura.columns)
print(df_candidatura_novo.columns)

df_candidatura_novo['idade_data_posse'] = df_candidatura_novo['idade_data_posse'].astype(int)

print(df_candidatura['idade_data_posse'].values)
print(df_candidatura_novo['idade_data_posse'].values)

# Calculando o log da idade
df_candidatura_novo['idade_data_posse_log'] = np.log(df_candidatura['idade_data_posse'])
print(df_candidatura_novo['idade_data_posse_log'].values)

# Calculando campo maluco
df_candidatura_novo['campo_maluco'] = df_candidatura_novo['idade_data_posse'] + df_candidatura_novo['idade_data_posse'] * 2
print(df_candidatura_novo['campo_maluco'].values)

print(f"Original:   {df_candidatura_novo['idade_data_posse'].values}")
print(f"Logarítimo: {df_candidatura_novo['idade_data_posse_log'].values}")
print(f"Maluco:     {df_candidatura_novo['campo_maluco'].values}")

# Elaborando um pouco mais

nome_qualquer = 'TEMYLLIS LIMA DA SILVA'

print(nome_qualquer.split(' ')[0])

def pega_primeiro_nome(nome):
    return nome.strip().split(' ')[0]

pega_primeiro_nome('Fabio Eduardo de Oliveira Medeiros')

print(df_candidatura_novo['nome'][0])

pega_primeiro_nome(df_candidatura_novo['nome'][0])

df_candidatura_novo['primeiro nome'] = df_candidatura_novo['nome'].apply(pega_primeiro_nome)

print(df_candidatura_novo[['nome', 'primeiro nome']])

print(df_candidatura_novo.columns)

df_candidatura_novo['provedor'] = df_candidatura_novo['email'].fillna('').apply(lambda x: x.rstrip(' ').split('@')[-1])

df_candidatura_novo.columns