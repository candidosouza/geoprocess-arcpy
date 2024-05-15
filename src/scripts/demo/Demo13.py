import arcpy
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 4\Shapefiles'

listFiles = arcpy.ListFiles('*.shp')
for shp in listFiles:
    print(shp)