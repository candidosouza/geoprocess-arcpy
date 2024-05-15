import arcpy

inp = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 1\Brasil.gdb\MUNICIPIOS'
inp2 = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 1\Brasil.gdb\RODOVIAS'
selecao = arcpy.SelectLayerByLocation_management(inp, 'INTERSECT', inp2)
arcpy.CopyFeatures_management(selecao, r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 1\Brasil.gdb\Mun_Rodov_PyCharm')
print('Script finalizado!')