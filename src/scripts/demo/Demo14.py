import arcpy

# configurar o diretório
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 4\Shapefiles'
dir = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 4'

# Criar o file geodatabase
gdb = arcpy.CreateFileGDB_management(dir, 'Conversao')

# Listar shapefiles
shpList = arcpy.ListFiles('*.shp')

# Converter para feature class de geodatabase
for shp in shpList:
    arcpy.FeatureClassToFeatureClass_conversion(shp, gdb, shp)
    print(f'{shp} convertido com sucesso para feature class de geodatabase!')
print('Script finalizado!')