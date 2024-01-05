import pandas as pd
import os
import sqlalchemy

# Configurando caminhos absolutos para todos os sistemas operacionais
path_src = os.path.join(os.path.abspath('.'), 'src') # Diretório dos códigos
# path_src = os.path.dirname(os.path.abspath(__file__)) # Diretório dos códigos
path_proj = os.path.dirname(path_src) # Diretório do projeto
path_data = os.path.join(path_proj, 'data') # Diretório dos dados

print(path_proj)
print(path_src)
print(path_data)

con = sqlalchemy.create_engine( "sqlite:///" + os.path.join(path_proj, 'brasilio.db'))
con.table_names()