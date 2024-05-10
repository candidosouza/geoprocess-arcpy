import os
import sys
import arcpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from settings.settings import Settings

# Configuração de ambiente
settings = Settings()
arcpy.env.overwriteOutput = True

# Declarando variáveis
aeroports = settings.INPUT_FEATURE + r'\AEROPORTOS'
input_buffer01 = input('Digite o valor do primeiro Buffer que deseja (metros): ')
aeroports_buffer01 = settings.GEODB_DESTINY + r'\AEROPORTOS_BUFFER_' + input_buffer01
print('Buffer 01 declarado...')

# Geração do buffer de acordo com a distância informada pelo usuário
arcpy.Buffer_analysis(aeroports, aeroports_buffer01, f'{input_buffer01} Meters')

# Declarando variáveis
input_buffer02 = input('Digite o valor do segundo Buffer que deseja (metros): ')
aeroports_buffer02 = settings.GEODB_DESTINY + r'\AEROPORTOS_BUFFER_' + input_buffer02
print('Buffer 02 declarado...')

# Geração do buffer de acordo com a distância informada pelo usuário
arcpy.Buffer_analysis(aeroports, aeroports_buffer02, f'{input_buffer02} Meters')

print(f'Script finalizado com sucesso. O buffer de {input_buffer01} metros e o buffer de {input_buffer02} metros,  foi gerado no geodatabase de saída!')
