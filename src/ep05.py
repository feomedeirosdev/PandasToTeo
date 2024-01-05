import pandas as pd
import os
import sqlalchemy
import sqlite3

# Configurando caminhos absolutos para todos os sistemas operacionais
path_src = os.path.join(os.path.abspath('.'), 'src') # Diretório dos códigos
path_src = os.path.dirname(os.path.abspath(__file__)) # Diretório dos códigos
path_proj = os.path.dirname(path_src) # Diretório do projeto
path_data = os.path.join(path_proj, 'data') # Diretório dos dados

print(path_proj)
print(path_src)
print(path_data)

con = sqlalchemy.create_engine( "sqlite:///" + os.path.join(path_proj, 'brasilio.db'))

# # # TENTATIVA DE CONEXÃO Nº 01
# con.table_names()

# # # TENTATIVA DE CONEXÃO Nº 02

# # Crie um objeto MetaData
# metadata = sqlalchemy.MetaData()

# # Carregue as informações da tabela associadas à conexão
# metadata.reflect(bind=con)

# # Obtenha os nomes das tabelas
# table_names = metadata.tables.keys()

# # Imprima os nomes das tabelas
# print(table_names)

# # # TENTATIVA DE CONEXÃO Nº 03

# # Use o Inspector para obter informações sobre as tabelas
# inspector = sqlalchemy.inspect(con)

# # Obtenha os nomes das tabelas
# table_names = inspector.get_table_names()

# # Imprima os nomes das tabelas
# print(table_names)

# # # TENTATIVA DE CONEXÃO Nº 04

# # Force uma atualização da engine
# con.connect().execute('SELECT 1')

# # Use o Inspector para obter informações sobre as tabelas
# inspector = sqlalchemy.inspect(con)

# # Obtenha os nomes das tabelas
# table_names = inspector.get_table_names()

# # Imprima os nomes das tabelas
# print(table_names)

# # # TENTATIVA DE CONEXÃO Nº 05

# # Execute uma consulta SQL simples para forçar a atualização
# con.execute('SELECT 1')

# # Use o Inspector para obter informações sobre as tabelas
# inspector = sqlalchemy.inspect(con)

# # Obtenha os nomes das tabelas
# table_names = inspector.get_table_names()

# # Imprima os nomes das tabelas
# print(table_names)

# # # TENTATIVA DE CONEXÃO Nº 06

# Imprima algumas informações sobre a conexão
print("Is Connected:", con.connect().closed)

# Use o Inspector para obter informações sobre as tabelas
inspector = sqlalchemy.inspect(con)

# Obtenha os nomes das tabelas
table_names = inspector.get_table_names()

# Imprima os nomes das tabelas
print("Final Table Names:", table_names)