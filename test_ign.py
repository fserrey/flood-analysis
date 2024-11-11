import requests
from owslib.wms import WebMapService


def check_ign_access():
    ign_url = "https://www.ign.es/wms-inspire/ign-base"

    try:
        response = requests.get(ign_url)
        if response.status_code == 200:
            print("Acceso exitoso a los datos del IGN.")
        else:
            print(f"Error al acceder a los datos del IGN. Código de estado: {response.status_code}")
    except Exception as e:
        print("Error al conectarse al servidor del IGN:", e)




def check_ign_data_access():
    wms_url = "https://www.ign.es/wms-inspire/ign-base"  # Cambia esto si necesitas otro servicio

    try:
        wms = WebMapService(wms_url)
        print("Conexión al servicio WMS del IGN exitosa.")

        # list layers
        layers = list(wms.contents)
        print("Capas disponibles:", layers)

        # IGNBaseOrto provides elevation info
        layer_name = "IGNBaseOrto"

        if layer_name in layers:
            print(f"Capa '{layer_name}' disponible en el servicio.")

            # layer info
            layer_info = wms[layer_name]
            print("Información de la capa:", layer_info.title, "-", layer_info.abstract)
        else:
            print(f"La capa '{layer_name}' no se encuentra en el servicio.")

    except Exception as e:
        print("Error al acceder a los datos del IGN:", e)


def check_ign_mde_access():
    wms_url = "https://servicios.idee.es/wms-inspire/mdt"

    try:
        wms = WebMapService(wms_url, version='1.3.0')
        print("Conexión al servicio WMS MDT del IGN exitosa.")

        # list layers
        layers = list(wms.contents)
        print("Capas disponibles:", layers)

        # capa 'EL.ElevationGridCoverage' para elevaciones
        layer_name = "EL.ElevationGridCoverage"

        if layer_name in layers:
            print(f"Capa '{layer_name}' disponible en el servicio.")

            # layer info
            layer_info = wms[layer_name]
            print("Información de la capa:", layer_info.title, "-", layer_info.abstract)
        else:
            print(f"La capa '{layer_name}' no se encuentra en el servicio.")

    except Exception as e:
        print("Error al acceder a los datos del IGN:", e)



# RUN
#check_ign_access()
#check_ign_data_access()
check_ign_mde_access()


