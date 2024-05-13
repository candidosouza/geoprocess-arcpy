# Importando bibliotecas
import os
import sys
import arcpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from settings.settings import Settings

print('Módulos importados...')

# Configuração de ambiente
settings = Settings()

# Cria um objeto de referência espacial com base no identificador EPSG
# spatial_reference = arcpy.SpatialReference(4674)  # EPSG code for SIRGAS 2000
spatial_reference = arcpy.SpatialReference(31977)  # EPSG code for SIRGAS 2000 datum 20S

arcpy.CreateFeatureclass_management(
    settings.GEODB_DESTINY,
    'MUNICIPIOS',
    'POLYGON',
    spatial_reference=spatial_reference,
    )

print('Script finalizado com sucesso!')