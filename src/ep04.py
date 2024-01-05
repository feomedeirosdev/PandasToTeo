import pandas as pd
import numpy as np
import os

# Definindo caminhos absolutos para todos os sistemas operacionais
path_src = os.path.join(os.path.abspath('.'), 'src')
path_src = os.path.dirname(os.path.abspath(__file__))
path_proj = os.path.dirname(path_src)
path_data = os.path.join(path_proj, 'data')
# print()
# print(path_proj)
# print(path_src)
# print(path_data)
# print()

pathfile_candidatura_csv = os.path.join(path_data, 'tb_candidatura_2018.csv')
# print(pathfile_candidatura_csv)
df_candidatura = pd.read_csv(pathfile_candidatura_csv, sep=';')
# df_candidatura = pd.read_csv('/home/medeiros/Documentos/PandasToTeo/data/tb_candidatura_2018.csv', sep=';')

print(df_candidatura)

# colunas_de_interesse = ['ano_eleicao',
#                        'data_eleicao',
#                        'descricao_eleicao',
#                        'nome_tipo_eleicao',
#                        'tipo_abrangencia_eleicao',
#                        'descricao_totalizacao_turno',
#                        'numero_turno',
#                        'descricao_ue',
#                        'sigla_ue',
#                        'sigla_uf',
#                        'cpf',
#                        'data_nascimento',
#                        'descricao_cor_raca',
#                        'descricao_estado_civil',
#                        'descricao_genero',
#                        'descricao_grau_instrucao',
#                        'descricao_nacionalidade',
#                        'descricao_ocupacao',
#                        'email',
#                        'nome',
#                        'nome_municipio_nascimento',
#                        'nome_social',
#                        'sigla_uf_nascimento',
#                        'titulo_eleitoral',
#                        'composicao_legenda',
#                        'nome_legenda',
#                        'nome_partido',
#                        'numero_partido',
#                        'sigla_legenda',
#                        'sigla_partido',
#                        'tipo_agremiacao',
#                        'concorre_reeleicao',
#                        'declara_bens',
#                        'descricao_cargo',
#                        'descricao_detalhe_situacao_candidatura',
#                        'descricao_situacao_candidatura',
#                        'despesa_maxima_campanha',
#                        'idade_data_eleicao',
#                        'idade_data_posse',
#                        'nome_urna',
#                        'numero_processo_candidatura',
#                        'numero_protocolo_candidatura',
#                        'numero_sequencial',
#                        'numero_urna',
#                        'pergunta']

df_candidatura['descricao_cargo'].unique()

########################
# INICIO DO EPISÓDIO 04 - Objetivo da aula: Encontrar a quantidade de deputados por estado, cor, raça, sexo, etc
########################

df_dep_estadual = df_candidatura[(df_candidatura['descricao_cargo'] == 'DEPUTADO ESTADUAL') &
                                 (df_candidatura['descricao_situacao_candidatura'] == 'APTO')]

# Taxa de aptos
print(df_dep_estadual.shape[0]) # Nº total de candidatos aptos
print(df_candidatura[df_candidatura['descricao_cargo'] == 'DEPUTADO ESTADUAL'].shape[0]) # Nº toatal de candidatos
print(f'Percentual de Deputados Estaduais Aptos: {(df_dep_estadual.shape[0] / df_candidatura[df_candidatura['descricao_cargo'] == 'DEPUTADO ESTADUAL'].shape[0]) * 100:.2f}%')

print(df_candidatura)
print(df_dep_estadual)

print(df_dep_estadual.shape) # Total
print(df_dep_estadual['cpf'].nunique()) # Não existe duplicatas

# AGRUPAMENTO

# Isso é um DataFrame pois estamos usando 'cpf', entretanto tem multindex 'sigla_uf' e 'descricao_genero'
agrupa_estado_genero = df_dep_estadual.groupby(['sigla_uf', 'descricao_genero'])[['cpf']].nunique() # df.groupby( [campos] ).[métricas].funcs() - sintaxe

# Desempilha os valores
df_estado_genero = agrupa_estado_genero.unstack() # Remove multindex das colunas, não necescita do .droplevel()

# Reseta o índice do DataFrame
df_estado_genero = df_estado_genero.reset_index()

print(agrupa_estado_genero)
print(df_estado_genero)

# IMPORTANDO MAIS DADOS

df_patrimonio = pd.read_excel(os.path.join(path_data, 'tb_declaracao_2018.xlsx'))
print(df_patrimonio.columns)

# Agrupando para saber o patrimonio total dos candidatos
df_patrimonio_candidato = (df_patrimonio.groupby(['numero_sequencial'])[['valor']]
                                        .sum()
                                        .reset_index())

df_patrimonio_candidato.columns

# Merge patrimonio
df_full = pd.merge(left = df_candidatura,
                   right = df_patrimonio_candidato,
                   how = 'left',
                   on = ['numero_sequencial'])

print(df_full.columns)

print(df_full)

# Achar o bolsonaro
df_full[df_full['nome'].apply(lambda x: 'BOLSONARO' in x)][['numero_sequencial', 'nome', 'valor']]

df_full[df_full['numero_sequencial'] == 280000614517][['nome', 'valor']]

# Descobrir o partido com o maior patrimônio médio por candidato

df_filtrado = (df_full[df_full['descricao_situacao_candidatura'] == 'APTO'] # filtra candidatos aptos
               .sort_values(['cpf', 'numero_turno']) # ordena por 'cpf' e 'numero_turno'
               .drop_duplicates('cpf', keep='first') # exclui linhas duplicadas com base apenas no 'cpf'
               .fillna({'valor': 0})) # preenche valores vazios no campo 'valor' com 0

# Verificação dos filtros
print()
print(df_filtrado.shape[0]) # retorna numero de linhas do DataFrame
print(df_filtrado['cpf'].nunique()) # retorna quantidade de 'cpf' distintos
print(df_filtrado['descricao_situacao_candidatura'].nunique()) # retorna quantidade de valores distintos no campo 'descricao_situacao_candidatura' (no caso somente o valor 'APTO)
print(df_filtrado['descricao_situacao_candidatura'].unique()) # retorna quais valores distintos no campo 'descricao_situacao_candidatura' (no caso somente o valor 'APTO)
print()

# Descobrindo os partidos mais ricos (ladrões)
df_partido = df_filtrado.groupby(['sigla_partido']).agg({'valor': ['sum', 'mean', 'median']})
df_partido.sort_values([('valor', 'mean')], inplace=True, ascending=False)
print(df_partido)