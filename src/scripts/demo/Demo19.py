import arcpy
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 5\CURITIBA.gdb'

academias = 'ACADEMIA_AO_AR_LIVRE'
bairros = 'BAIRROS'
out1 = r'in_memory\output1'
out2 = r'in_memory\output2'

arcpy.SummarizeWithin_analysis(bairros, academias, out1)
arcpy.Sort_management(out1, out2, [['Point_Count', 'DESCENDING']])

campos = ['NOME', 'Point_Count']

with arcpy.da.SearchCursor(out2, campos) as cursor:
    for linhas in cursor:
        if linhas[1] >= 1:
            print(f'{linhas[0]}: {linhas[1]} academias')
del cursor
print('Script finalizado!')