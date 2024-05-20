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
fields = ['NOME_ABREV', 'NOME_HOSP']

# Usar o updateCursor para atualizar a coluna 'NOME_HOSP'
with arcpy.da.UpdateCursor(hospital, fields) as ucursor:
    for lines in ucursor:
        lines[1] = lines[0].upper()
        ucursor.updateRow(lines)
del ucursor
