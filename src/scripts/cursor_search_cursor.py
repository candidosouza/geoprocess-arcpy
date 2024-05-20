# Importando bibliotecas
import os
import sys
import arcpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from settings.settings import Settings

print('Módulos importados...')

# Configuração de ambiente
settings = Settings()

# Configuração de ambiente
arcpy.env.workspace = settings.GEODB_DESTINY
hospital = settings.INPUT_FEATURE + r'\HOSPITAL.shp'
fields = ['NOME', 'BAIRRO', 'REGIONAL', 'DEP_ADMIN']

# # descobrir os nomes dos campos
# list_fc = arcpy.ListFields(hospital)
# for field in list_fc:
#     print(f'{field.name}', end='; ')

# Usar SearchCursor simples para consultar a tabela de atributos
# with arcpy.da.SearchCursor(hospital, ['NOME', 'BAIRRO', 'REGIONAL', 'DEP_ADMIN']) as scursor:
#     for lines in scursor:
#         print(f'{lines[0]}, {lines[1]}, {lines[2]}, {lines[3]}')
# del scursor

# Usar um curso do tipo Search com um filtro
exp = "DEP_ADMIN = 'Particular'"
c = 0
with arcpy.da.SearchCursor(hospital, fields) as scursor:
    for line in scursor:
        if line[3] == 'Particular':
            print(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}')
            c += 1
del scursor
print(' - '*30)
print(f'Total de linhas retornadas: {c}')