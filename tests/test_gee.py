import ee

def check_gee_access():
    try:
        # auth and initiate GEE
        ee.Authenticate()
        ee.Initialize()
        print("Conectado a Google Earth Engine!")

        # sample Spain region
        area = ee.Geometry.Rectangle([-10.0, 35.0, 5.0, 45.0])

        # Sentinel-1 access check
        sentinel1 = ee.ImageCollection("COPERNICUS/S1_GRD") \
            .filterBounds(area) \
            .filterDate('2023-01-01', '2023-12-31') \
            .select(['VV', 'VH'])

        #
        image_count = sentinel1.size().getInfo()
        print(f"Número de imágenes de Sentinel-1 encontradas: {image_count}")

    except Exception as e:
        print("Error al conectarse a Google Earth Engine:", e)

#
check_gee_access()
