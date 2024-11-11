import time
import os
import rasterio
from owslib.wms import WebMapService
import numpy as np
from PIL import Image
from io import BytesIO

# Configuración inicial
wms_url = "https://servicios.idee.es/wms-inspire/mdt"
wms = WebMapService(wms_url, version='1.3.0')

# Parámetros para la solicitud GetMap
layer_name = "EL.ElevationGridCoverage"
bbox = (-3.7038, 40.4168, -3.6038, 40.5168)  # Ejemplo: coordenadas para una región en Madrid
crs = "EPSG:4326"
width, height = 800, 600
image_format = "image/png"

def process_in_memory():
    """Procesa la imagen en memoria sin guardarla en disco."""
    start_time = time.time()

    # Realizar la solicitud GetMap
    response = wms.getmap(
        layers=[layer_name],
        srs=crs,
        bbox=bbox,
        size=(width, height),
        format=image_format,
        transparent=True
    )

    # Leer la imagen en memoria
    with rasterio.MemoryFile(response.read()) as memfile:
        with memfile.open() as dataset:
            elevation_data = dataset.read(1)  # Lee la primera banda

    end_time = time.time()
    print(f"Tiempo de procesamiento en memoria: {end_time - start_time:.2f} segundos")
    return elevation_data

def process_with_download():
    """Descarga la imagen y la procesa desde el disco."""
    start_time = time.time()

    # Realizar la solicitud GetMap y guardar en disco
    response = wms.getmap(
        layers=[layer_name],
        srs=crs,
        bbox=bbox,
        size=(width, height),
        format=image_format,
        transparent=True
    )
    image_path = "../data/raw/elevation_image.png"
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    with open(image_path, "wb") as file:
        file.write(response.read())

    # Leer la imagen desde el disco
    with rasterio.open(image_path) as dataset:
        elevation_data = dataset.read(1)  # Lee la primera banda

    # Eliminar el archivo descargado
    os.remove(image_path)

    end_time = time.time()
    print(f"Tiempo de procesamiento con descarga: {end_time - start_time:.2f} segundos")
    return elevation_data


# Ejecutar las pruebas
print("Ejecutando prueba de procesamiento en memoria...")
elevation_data_memory = process_in_memory()

print("\nEjecutando prueba de procesamiento con descarga...")
elevation_data_download = process_with_download()

# Comparar los resultados
if np.array_equal(elevation_data_memory, elevation_data_download):
    print("\n¡Los datos de elevación son iguales en ambos métodos!")
else:
    print("\nLos datos de elevación son diferentes. Revisa el código o la precisión de los datos.")

