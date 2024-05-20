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


# Cursor de inserção de um novo ponto
cursor = arcpy.da.InsertCursor(hospital, ['NOME', 'SHAPE@XY'])
line = ['Zilda Arns', (671488.25,7177418.35)]
cursor.insertRow(line)
del cursor
