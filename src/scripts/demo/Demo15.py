import arcpy

# Configuração de ambiente
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 5\CURITIBA.gdb'
fc = 'HOSPITAL'
campos = ['NOME', 'BAIRRO', 'REGIONAL', 'DEP_ADMIN']

# Descobrir o nome dos campos
# lista = arcpy.ListFields(fc)
# for campos in lista:
#     print(f'{campos.name}', end='; ')

# Usar SearchCursor simples para consultar a tabela de atributos
# with arcpy.da.SearchCursor(fc, ['NOME', 'BAIRRO', 'REGIONAL', 'DEP_ADMIN']) as scursor:
#     for linhas in scursor:
#         print(f'{linhas[0]}, {linhas[1]}, {linhas[2]}, {linhas[3]}')
# del scursor

# Usar um curso do tipo Search com um filtro
exp = "DEP_ADMIN = 'Particular'"
c = 0
with arcpy.da.SearchCursor(fc, campos) as scursor:
    for linhas in scursor:
        if linhas[3] == 'Particular':
            print(f'{linhas[0]}, {linhas[1]}, {linhas[2]}, {linhas[3]}')
            c += 1
del scursor
print(' - '*30)
print(f'Total de linhas retornadas: {c}')