import arcpy

# Configuração de ambiente
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 5\CURITIBA.gdb'
fc = 'HOSPITAL'

# Cursor de inserção de um novo ponto
cursor = arcpy.da.InsertCursor(fc, ['NOME', 'SHAPE@XY'])
linha = ['Zilda Arns', (671488.25,7177418.35)]
cursor.insertRow(linha)
del cursor

# Cursor com método delete
with arcpy.da.UpdateCursor(fc, 'NOME') as ucursor:
    for linhas in ucursor:
         if linhas[0] == 'Zilda Arns':
             ucursor.deleteRow()
del ucursor