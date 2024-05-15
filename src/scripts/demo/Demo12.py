import arcpy
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 4'

listGDB = arcpy.ListWorkspaces('*', 'FileGDB')
for gdb in listGDB:
    print(gdb)
