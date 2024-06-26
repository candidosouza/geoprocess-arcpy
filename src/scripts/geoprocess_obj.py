# Importando bibliotecas
import os
import sys
import arcpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from settings.settings import Settings

print('Módulos importados...')

# Configuração de ambiente
settings = Settings()

# Configuração de ambiente
arcpy.env.workspace = settings.GEODB_DESTINY
arcpy.env.overwriteOutput = True

# obtendo as feições
academies = settings.INPUT_FEATURE + r'\ACADEMIA_AO_AR_LIVRE.shp'
neighborhoods = settings.INPUT_FEATURE + r'\BAIRROS.shp'

# saidas em memória
output1 = r'in_memory\output1'
output2 = r'in_memory\output2'


print('Copiando feiçao...')
new_layer = settings.GEODB_DESTINY + r'\BAIRROS'
# copiando feiçao
arcpy.CopyFeatures_management(neighborhoods, new_layer)
print('Feiçao copiada. Criando novo campo na feiçao...')

#criando novo campo na feição
new_field_name = "ACADEMIAS"
# Define o tipo de dados do novo campo (e.g., TEXT, FLOAT, DOUBLE, SHORT, LONG, DATE, BLOB, RASTER, GUID)
field_type = "DOUBLE"
# Define outras propriedades do campo, se necessário (opcional)
field_precision = ""  # Use para campos numéricos
field_scale = ""      # Use para campos numéricos
field_length = 50     # Use para campos de texto
field_alias = "QTD ACADEMIAS"  # Alias do campo
field_is_nullable = "NULLABLE"  # O campo pode ser nulo ou não
field_is_required = "NON_REQUIRED"  # O campo é obrigatório ou não
field_domain = ""  # Use se houver um domínio associado ao campo


print('Criando novo campo...')

# Adiciona o campo ao feature class
arcpy.AddField_management(
    f'{new_layer}.shp',
    new_field_name,
    field_type,
    field_precision,
    field_scale,
    field_length,
    field_alias,
    field_is_nullable,
    field_is_required,
    field_domain
)
print(f"Campo '{new_field_name}' adicionado com sucesso à feição '{new_layer}'")

# Calcula a quantidade de academias por bairro

"""
SummarizeWithin_analysis:
Sobrepõe uma camada de polígono com outra camada para resumir o número de pontos,
o comprimento das linhas ou a área dos polígonos dentro de cada polígono e calcular
estatísticas de campo de atributo sobre as feições dentro dos polígonos.
"""
arcpy.SummarizeWithin_analysis(neighborhoods, academies, output1)
arcpy.Sort_management(output1, output2, [['Point_Count', 'DESCENDING']])


fields = ['NOME', 'Point_Count']

with arcpy.da.SearchCursor(output2, fields) as cursor:
    for lines in cursor:
        # if lines[0] >= 1:
        cursor_update = arcpy.da.UpdateCursor(new_layer, ['ACADEMIAS'])
        # lines[0] == lines[1]
        value = 1
        cursor_update.updateRow(lines)

del cursor
print('Script finalizado!')
