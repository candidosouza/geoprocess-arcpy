# Importando bibliotecas
import os
import sys
import arcpy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from settings.settings import Settings

print('Módulos importados...')

# Configuração de ambiente
settings = Settings()

arcpy.env.overwriteOutput = True

# Declarar as variáveis
aero = settings.INPUT_FEATURE + r'\AEROPORTOS'
dist = int(input('Digite a distância do Buffer (metros): '))
outp = settings.GEODB_DESTINY + r'\AEROPORTOS_'
print('Variáveis foram declaradas...')

# Gerar buffer
arcpy.Buffer_analysis(aero, outp, f'{dist} Meters')

# Usar a função Describe
desc = arcpy.Describe(outp)

# Prints dos resultados
print(f'Processo concluído! Descrição do resultado:\n'
      f'Tipo de Geometria: {desc.shapeType}\n'
      f'Distância do buffer: {dist} metros\n'
      f'Sistema de coordenadas: {desc.spatialReference.name}\n'
      f'{" - "*30}\n'
      f'Script finalizado!')
