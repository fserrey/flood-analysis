import time
import json
import os
import rasterio
from owslib.wms import WebMapService

wms_url = "https://servicios.idee.es/wms-inspire/mdt"
wms = WebMapService(wms_url, version='1.3.0')

layer_name = "EL.ElevationGridCoverage"
crs = "EPSG:4326"
image_format = "image/png"
width, height = 1000, 1000

full_bbox = (-5.0, 35.0, 5.0, 45.0)  # test area
num_subregions = 4  # Número de divisiones en cada dirección


def divide_bbox(bbox, num_subregions):
    """Divide un bbox en subregiones más pequeñas."""
    minx, miny, maxx, maxy = bbox
    step_x = (maxx - minx) / num_subregions
    step_y = (maxy - miny) / num_subregions

    subregions = []
    for i in range(num_subregions):
        for j in range(num_subregions):
            sub_minx = minx + i * step_x
            sub_miny = miny + j * step_y
            sub_maxx = sub_minx + step_x
            sub_maxy = sub_miny + step_y
            subregions.append((sub_minx, sub_miny, sub_maxx, sub_maxy))

    return subregions


def extract_data_subregion(subregion, retries=3, timeout=60):
    """extracción por subregión"""
    for attempt in range(retries):
        try:
            response = wms.getmap(
                layers=[layer_name],
                srs=crs,
                bbox=subregion,
                size=(width, height),
                format=image_format,
                transparent=True,
                timeout=timeout
            )

            with rasterio.MemoryFile(response.read()) as memfile:
                with memfile.open() as dataset:
                    elevation_data = dataset.read(1)  # lectura banda 1

            print(f"Subregión {subregion} procesada con éxito en intento {attempt + 1}")
            return elevation_data
        except Exception as e:
            print(f"Error al procesar subregión {subregion} en intento {attempt + 1}: {e}")
            time.sleep(5)  #
    print(f"Subregión {subregion} falló después de {retries} intentos")
    return None


def main():
    subregions = divide_bbox(full_bbox, num_subregions)
    # subregión
    for idx, subregion in enumerate(subregions):
        elevation_data = extract_data_subregion(subregion)
        if elevation_data is not None:
            print(f"Datos procesados para subregión {idx}")
        else:
            print(f"Fallo al procesar subregión {idx}")


# Ejecutar el extractor
main()
