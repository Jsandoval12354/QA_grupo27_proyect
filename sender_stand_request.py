
import requests
from configuration import BASE_URL
from data import CREATE_USER_PAYLOAD

def enviar_get_request(endpoint, token_auth=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {}
    if token_auth:
        headers["Authorization"] = token_auth
    response = requests.get(url, headers=headers)
    return response

def enviar_post_request(endpoint, cuerpo_request=None, encabezados_request=None):
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=cuerpo_request, headers=encabezados_request)
    return response

def enviar_put_request(endpoint, cuerpo_request=None, token_auth=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {}
    if token_auth:
        headers["Authorization"] = token_auth
    response = requests.put(url, json=cuerpo_request, headers=headers)
    return response

def enviar_delete_request(endpoint, token_auth=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {}
    if token_auth:
        headers["Authorization"] = token_auth
    response = requests.delete(url, headers=headers)
    return response

def obtener_token_usuario_auth():
    response = enviar_post_request("/api/v1/users", cuerpo_request=CREATE_USER_PAYLOAD)
    if response.status_code == 201:
        return response.json().get("authToken")
    else:
        print(f"Error al crear usuario: {response.status_code} - {response.text}")
        return None

def crear_nuevo_kit(datos_kit, token_auth=None):
    encabezados = {}
    if token_auth:
        encabezados["Authorization"] = token_auth
    response = enviar_post_request("/api/v1/kits", cuerpo_request=datos_kit, encabezados=encabezados)
    return response

def actualizar_kit(kit_id, datos_actualizacion, token_auth=None):
    endpoint = f"/api/v1/kits/{kit_id}"
    return enviar_put_request(endpoint, cuerpo_request=datos_actualizacion, token_auth=token_auth)

def eliminar_kit(kit_id=7, token_auth=None):
    endpoint = f"/api/v1/kits/{kit_id}"
    return enviar_delete_request(endpoint, token_auth=token_auth)