from owslib.wms import WebMapService
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO


def get_elevation_map():
    # WMS MDT del IGN
    wms_url = "https://servicios.idee.es/wms-inspire/mdt"
    wms = WebMapService(wms_url, version='1.3.0')

    layer_name = "EL.ElevationGridCoverage"
    bbox = (-3.7038, 40.4168, -3.6038, 40.5168)  # madrid
    crs = "EPSG:4326"
    width = 800
    height = 600
    image_format = "image/png"

    response = wms.getmap(
        layers=[layer_name],
        srs=crs,
        bbox=bbox,
        size=(width, height),
        format=image_format,
        transparent=True
    )

    # response as img
    img = Image.open(BytesIO(response.read()))

    # vizz
    plt.figure(figsize=(10, 8))
    plt.imshow(img)
    plt.axis('off')
    plt.title("Modelo Digital del Terreno - Elevación (Ejemplo en Madrid)")
    plt.show()


get_elevation_map()
