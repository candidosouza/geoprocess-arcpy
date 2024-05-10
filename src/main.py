import arcpy
from settings import Settings

# Configuração de ambiente
settings = Settings()
arcpy.env.overwriteOutput = True


# Declarando variáveis
aeroportos = settings.INPUT_FEATURE + r'\AEROPORTOS'
dist_buffer = input('Digite o valor do Buffer que deseja (km): ')
output = settings.GEODB_DESTINY + r'\AEROPORTOS_BUFFER'
print('Variáveis declaradas...')

# Geração do buffer de acordo com a distância informada pelo usuário
arcpy.Buffer_analysis(aeroportos, output, f'{dist_buffer} Kilometers')
print(f'Script finalizado com sucesso. O buffer de {dist_buffer} km foi gerado no geodatabase de saída!')

if __name__ == '__main__':

    print(settings.GEODB_DESTINY)