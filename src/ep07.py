import sqlite3
from sqlalchemy import create_engine

# Caminho para o banco de dados
db_path = 'sqlite:///' + '/home/medeiros/Documentos/PandasToTeo/data/brasilio.db'

# Criar uma engine de conexão
engine = create_engine(db_path)

# Nome da tabela que você deseja consultar
table_name = 'tb_candidatura'

# Consulta SQL para obter todos os registros da tabela
query = f'SELECT * FROM {table_name};'

# Executar a consulta
result = engine.execute(query)

# Obter os resultados como uma lista de dicionários
rows = [dict(row) for row in result]

# Imprimir os resultados
print(rows)