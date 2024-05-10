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
dist_buffer1 = input('Digite o valor do primeiro Buffer que deseja (metros): ')
output1 = settings.GEODB_DESTINY + r'\AEROPORTOS_BUFFER_' + dist_buffer1
print('Variáveis declaradas...')

# Geração do buffer de acordo com a distância informada pelo usuário
arcpy.Buffer_analysis(aeroportos, output1, f'{dist_buffer1} Meters')

dist_buffer2 = input('Digite o valor do segundo Buffer que deseja (metros): ')
output2 = settings.GEODB_DESTINY + r'\AEROPORTOS_BUFFER_' + dist_buffer2
print('Variáveis declaradas...')

# Geração do buffer de acordo com a distância informada pelo usuário
arcpy.Buffer_analysis(aeroportos, output2, f'{dist_buffer2} Meters')

print(f'Script finalizado com sucesso. O buffer de {dist_buffer1} metros e o buffer de {dist_buffer2} metros,  foi gerado no geodatabase de saída!')