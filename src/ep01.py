import pandas as pd

# # Séries
# s_receita = pd.Series( name = 'receita', data = [1, 4, 10, 'Fabio', None, True, '3'] )
# print(s_receita)

# # DataFrame
# dados = {'nome': ['Fabio', 'Eduardo', 'Oliveira', 'Medeiros'],
#          'sobrenome': ['Supremo', 'Magnífico', 'Show', 'Phoda'],
#          'idade': [36, 45, 23, 71]}
# df_dados = pd.DataFrame(dados)
# print(df_dados)

#######################################################################################

# Início da aula

# Importando dados com pandas
df_candidatura = pd.read_csv('/home/medeiros/Documentos/PandasToTeo/data/tb_candidatura_2018.csv', sep=';')
df_declaracao = pd.read_excel('/home/medeiros/Documentos/PandasToTeo/data/tb_declaracao_2018.xlsx')

# Exibe Nº primeiras linhas 
df_candidatura.head(3)

# Exibe Nº últimas linhas 
df_candidatura.tail(3)

# Exibe (linha, coluna) do DataFrame
df_candidatura.shape

# Exibe colunas do DataFrame
df_candidatura.columns

# Navegando...

df_candidatura[['ano_eleicao', 'nome', 'cpf']].head()

df_candidatura['nome'][4] # df[column][index]

df_candidatura.info()

df_candidatura.iloc[0:2]