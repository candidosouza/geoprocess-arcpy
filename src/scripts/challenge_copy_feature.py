# Importando bibliotecas
import os
import sys
import arcpy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from settings.settings import Settings

print('Módulos importados...')

# Configuração de ambiente
settings = Settings()

# Declarar as variáveis
aero = settings.INPUT_FEATURE + r'\AEROPORTOS'
muni = settings.INPUT_FEATURE + r'\MUNICIPIOS'
dist = int(input('Digite a distância (metros): '))
outp = settings.GEODB_DESTINY + r'\MUNICIPIOS_AERO'
print('Variáveis foram declaradas...')

# Usar função Select Layer by Location
selc = arcpy.SelectLayerByLocation_management(muni,
                                              'INTERSECT',
                                              aero, f'{dist} Meters')
print('Selecionando por localização...')

# Usar a função Copy Features
arcpy.CopyFeatures_management(selc, outp)
print(f'Exportando resultado\nScript finalizado!\nResultado disponível em: {outp}')