# Importar as bibliotecas
import arcpy

# Configuração de ambiente
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 3\BRASIL.gdb'
arcpy.env.overwriteOutput = True

# Trabalhando com variáveis
cam = input('Digite o nome da Feature Class: ')

# Usando a da.Describe
desc = arcpy.da.Describe(cam)
# print(desc)

print(desc['catalogPath'])
print(desc['dataType'])