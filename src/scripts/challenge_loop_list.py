# Importando bibliotecas
import arcpy
print('Módulos importados...')

# Configuração de ambiente
arcpy.env.workspace = r'C:\EsriTraining\PYTS\Desafios\CountyData.gdb'

# Declarar variáveis
cam = 'ParcelPts'
c = 0

# Usar a função ListFields
col = arcpy.ListFields(cam)
for campos in col:
    print(f'{campos.name} -> {campos.type}')
    c += 1
print(f'Total de colunas: {c}')