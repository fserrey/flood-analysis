import time
import numpy as np
from owslib.wms import WebMapService
import rasterio

wms_url = "https://servicios.idee.es/wms-inspire/mdt"
wms = WebMapService(wms_url, version='1.3.0')

layer_name = "EL.ElevationGridCoverage"
bbox = (-5.0, 35.0, 5.0, 45.0)  # bigger area
crs = "EPSG:4326"
width, height = 4000, 4000  # hgher resolution
image_format = "image/png"

def process_large_volume_locally():
    """test locally large volumen"""
    start_time = time.time()

    response = wms.getmap(
        layers=[layer_name],
        srs=crs,
        bbox=bbox,
        size=(width, height),
        format=image_format,
        transparent=True,
        timeout=60
    )

    # leer imagen en memoria
    with rasterio.MemoryFile(response.read()) as memfile:
        with memfile.open() as dataset:
            elevation_data = dataset.read(1)  #  banda 1

    end_time = time.time()
    print(f"Tiempo de lectura local para mayor volumen: {end_time - start_time:.2f} segundos")
    return elevation_data

print("Ejecutando prueba local para mayor volumen...")
elevation_data_local = process_large_volume_locally()
