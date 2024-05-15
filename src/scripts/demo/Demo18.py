import arcpy

# Configuração de ambiente
arcpy.env.workspace = r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Aula 5\CURITIBA.gdb'
fc = 'HOSPITAL'

# Variáveis
exp = "DEP_ADMIN = 'Particular'"
c = 0
cabecalho = ['Nome, Bairro, Regional, Departamento_Admin']

# Usar o searchCursor
with arcpy.da.SearchCursor(fc, ['NOME', 'BAIRRO', 'REGIONAL', 'DEP_ADMIN'], where_clause=exp) as scursor:
    for linhas in scursor:
        itens = (f'{linhas[0]}, {linhas[1]}, {linhas[2]}, {linhas[3]}')
        cabecalho.append(itens)
        c += 1
del scursor
print(' - '*30)
print(f'Total de linhas retornadas: {c}')
print(' - '*30)

# Exportar para *csv
corpoTexto = ';'.join(cabecalho)
csvFile = open(r'C:\Users\ivan.leonardi\OneDrive - Imagem Geosistemas e Comercio LTDA\Área de Trabalho\PYTS\Exemplos\Hospitais_Privados.csv', 'w')
csvFile.write(corpoTexto)
csvFile.close()
print('Script finalizado! Seu csv foi exportado com sucesso.')