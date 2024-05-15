# Importar as bibliotecas
import arcpy

# Configuração de ambiente
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 3\BRASIL.gdb'
arcpy.env.overwriteOutput = True

# Trabalhando com variáveis
cam = input('Digite o nome da Feature Class: ')

# Trabalhando com a função Desribe
desc = arcpy.Describe(cam)

# print(f'Tipo de geometria: {desc.shapeType}\nCaminho para o item: {desc.path}\nSRC: {desc.spatialReference.name}\nCódigo EPSG: {desc.spatialReference.factoryCode}')
arcpy.CreateFeatureclass_management(desc.path, f'{cam}_NOVO', desc.shapeType, cam, spatial_reference=desc.spatialReference)
print(f'Script finalizado. A camada {cam}_NOVO foi gerada no diretório {desc.path}')