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


# Cursor com método delete
with arcpy.da.UpdateCursor(fc, 'NOME') as ucursor:
    for lines in ucursor:
         if lines[0] == 'Zilda Arns':
             ucursor.deleteRow()
del ucursor