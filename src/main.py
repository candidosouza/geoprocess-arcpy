import arcpy
from settings import Settings

# Configuração de ambiente
settings = Settings()

# arcpy: É o módulo principal do ArcPy, que fornece acesso a várias ferramentas e funcionalidades do ArcGIS.
# arcpy.env: env é um submódulo de arcpy que controla configurações e ambientes no ArcGIS.
# arcpy.env.workspace: É uma propriedade do ambiente (env) que especifica o diretório ou banco de dados geoespacial no qual todas as operações subsequentes serão realizadas.
arcpy.env.workspace = settings.GEODB_DESTINY

# arcpy.env.overwriteOutput: É uma propriedade do ambiente (env) que determina se as saídas existentes serão sobregravadas/substituídos quando forem executadas operações de processamento geoespacial.
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