import arcpy
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 4\Brasil.gdb'

fdList = arcpy.ListFields('RODOVIAS', '', '')
quantidade = 0

for campos in fdList:
    quantidade += 1
    print(f'{campos.name} é do tipo {campos.type} e tem comprimento de {campos.length}')
print(f'Quantidade de colunas na camada: {quantidade}')
