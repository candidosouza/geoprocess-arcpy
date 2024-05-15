import arcpy
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 5\CURITIBA.gdb'

# Criar um cursor para acessar a geometria e o nome dos bairros
fc = 'BAIRROS'
c = 0
cursor = arcpy.da.SearchCursor(fc, ['SHAPE@', 'NOME'])
for bairros in cursor:
    # Usar o getPart para retornar uma array com os objetos de pontos para cada parte
    for poligonos in bairros[0].getPart():
        # print(f'{bairros[1]}: {poligonos.count}')
        for pts in poligonos:
            print(f'X: {pts.X}; Y: {pts.Y}')
            c += 1
del cursor
print(f'Total de vértices para a camada: {c}')
