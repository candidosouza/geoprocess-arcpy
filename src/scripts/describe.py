import os
import sys
import arcpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from settings.settings import Settings

# Configuração de ambiente
settings = Settings()
arcpy.env.overwriteOutput = True


# Declarando variáveis
aeroportos = settings.INPUT_FEATURE + r'\AEROPORTOS'

desc = arcpy.Describe(aeroportos)
print(f'Descricão: {desc.name}')
print(f'Tipo de objeto: {desc.shapeType}')
print(f'Caminho: {desc.path}')
print(f'Campos de atributos: {desc.catalogPath}')
print(f'Sistema de coordenadas: {desc.spatialReference.name}')
