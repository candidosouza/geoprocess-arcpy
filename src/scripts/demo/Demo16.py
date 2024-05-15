import arcpy

# Configuração de ambiente
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 5\CURITIBA.gdb'
fc = 'HOSPITAL'

# Add uma nova coluna na tabela de atributos
arcpy.AddField_management(fc, 'NOME_HOSP', field_type='TEXT', field_precision=50)

# Campos que serão trabalhados
campos = ['NOME_ABREV', 'NOME_HOSP']

# Usar o updateCursor para atualizar a coluna 'NOME_HOSP'
with arcpy.da.UpdateCursor(fc, campos) as ucursor:
    for linhas in ucursor:
        linhas[1] = linhas[0].upper()
        ucursor.updateRow(linhas)
del ucursor