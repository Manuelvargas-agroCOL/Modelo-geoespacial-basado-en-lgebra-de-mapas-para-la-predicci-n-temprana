import ee
import geemap
import os

ee.Initialize(project='geomaticageneral2026')
colombia = ee.Geometry.Rectangle([-79, -4, -67, 13])

# Intentemos con la versión directa del Atlas de Suelos
suelo = ee.Image("projects/soilgrids-isric/phh2o_mean").select(0).clip(colombia)

ruta_carpeta = r"C:\Users\manuu\OneDrive\Documentos\UNIVERSIDAD\GEOMATICA\CURSO\GeomaticaGeneral2026"

print("Descargando pH del suelo (intento final)...")
geemap.ee_export_image(suelo, filename=os.path.join(ruta_carpeta, "colombia_ph_suelo.tif"), scale=2000, region=colombia)
print("✅ ¡REVISADO! Si sale 'Data downloaded', ya puedes cerrar VS Code.")