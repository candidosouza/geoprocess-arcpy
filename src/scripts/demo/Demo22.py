import arcpy
import csv
import numpy

arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 5\CURITIBA.gdb'
arcpy.env.overwriteOutput = True

# Ler coordenadas a partir do arquivo CSV e criar o objeto geometrico de linha
file = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 6\RioBarigui_XYCoords.csv'
csvFile = open(file)
csvReader = csv.reader(csvFile)

# Inicializar a array de pontos fora do loop para evitar repetições
ary = arcpy.Array()

for linha in csvReader:
    x = float(linha[0])
    y = float(linha[1])
    pnt = arcpy.Point(x, y)
    ary.append(pnt)

# Exportando o rio
geomRio = arcpy.Polyline(ary)
fc = arcpy.CopyFeatures_management(geomRio, 'RioBarigui')
arcpy.DefineProjection_management(fc, 31982)

# Criando amostras
amostras = numpy.arange(0, 1.25, 0.25)
print(amostras)

# Gerar coordenadas a partir das porcentagens do rio
for local in amostras:
    amostrasP = geomRio.positionAlongLine(local, True)
    print(f'{local*100:.0f}% -> ponto inserido na localização X: {amostrasP.centroid.X}; Y: {amostrasP.centroid.Y}' )

# Criar uma feature class em branco do tipo ponto
arcpy.CreateFeatureclass_management(r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 5\CURITIBA.gdb',
                                    'AmostrasAgua', 'Point', spatial_reference=31982)
print(f'Feature class criada no gdb')

cursor = arcpy.da.InsertCursor('AmostrasAgua', 'Shape@XY')
for local in amostras:
    amostrasP = geomRio.positionAlongLine(local, True)
    cursor.insertRow([(amostrasP.centroid.X, amostrasP.centroid.Y)])
del cursor
print('Script finalizado')