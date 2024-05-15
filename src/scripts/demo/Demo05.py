# Importando biblioteca arcpy
import arcpy
print('Bibliotecas importadas...')

# Configuração de ambiente
arcpy.env.overwriteOutput = True

# Declarando variáveis
aeroportos = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 3\BRASIL.gdb\AEROPORTOS'
dist_buffer = input('Digite o valor do Buffer que deseja (km): ')
output = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 3\BRASIL.gdb\AEROPORTOS_BUFFER'
print('Variáveis declaradas...')

# Geração do buffer de acordo com a distância informada pelo usuário
arcpy.Buffer_analysis(aeroportos, output, f'{dist_buffer} Kilometers')
print(f'Script finalizado com sucesso. O buffer de {dist_buffer} km foi gerado no geodatabase de saída!')