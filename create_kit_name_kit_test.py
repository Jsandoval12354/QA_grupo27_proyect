import pytest
from sender_stand_request import obtener_token_usuario_auth, crear_nuevo_kit, enviar_get_request, actualizar_kit, eliminar_kit
from data import KIT_TEST_DATA, UPDATE_KIT_DATA

def verificar_respuesta_positiva(response, codigo_esperado=201):
    assert response.status_code == codigo_esperado
    assert response.json().get("name") is not None

def verificar_respuesta_negativa_codigo_400(response):
    assert response.status_code == 400

def test_crear_kit_con_nombre_valido():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = crear_nuevo_kit(KIT_TEST_DATA["valid_name_kit"], token_auth)
        verificar_respuesta_positiva(response)

def test_crear_kit_con_nombre_largo_valido():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = crear_nuevo_kit(KIT_TEST_DATA["long_valid_name_kit"], token_auth)
        verificar_respuesta_positiva(response)

def test_crear_kit_con_nombre_largo_invalido():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = crear_nuevo_kit(KIT_TEST_DATA["invalid_long_name_kit"], token_auth)
        verificar_respuesta_negativa_codigo_400(response)

def test_crear_kit_con_caracteres_especiales():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = crear_nuevo_kit(KIT_TEST_DATA["special_chars_kit"], token_auth)
        verificar_respuesta_positiva(response)

def test_crear_kit_con_espacios_en_nombre():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = crear_nuevo_kit(KIT_TEST_DATA["spaces_kit_name"], token_auth)
        verificar_respuesta_positiva(response)

def test_crear_kit_con_numeros_en_nombre():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = crear_nuevo_kit(KIT_TEST_DATA["numbers_kit_name"], token_auth)
        verificar_respuesta_positiva(response)

def test_crear_kit_con_nombre_vacio():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = crear_nuevo_kit(KIT_TEST_DATA["empty_kit_name"], token_auth)
        verificar_respuesta_negativa_codigo_400(response)

def test_crear_kit_con_campo_nombre_faltante():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = crear_nuevo_kit(KIT_TEST_DATA["missing_kit_name"], token_auth)
        verificar_respuesta_negativa_codigo_400(response)

def test_obtener_todos_los_kits():
    token_auth = obtener_token_usuario_auth()
    if token_auth:
        response = enviar_get_request("/api/v1/kits", token_auth)
        assert response.status_code == 200  # Asumiendo código 200 para éxito

def test_actualizar_un_kit():
    token_auth = obtener_token_usuario_auth()
    kit_id_a_actualizar = 1  # Asumiendo un ID existente para actualizar
    if token_auth:
        response = actualizar_kit(kit_id_a_actualizar, UPDATE_KIT_DATA, token_auth)
        assert response.status_code == 200  # Asumiendo código 200 para éxito
        assert response.json().get("name") == UPDATE_KIT_DATA["name"] # Asumiendo que la respuesta incluye el nombre actualizado

def test_eliminar_un_kit():
    token_auth = obtener_token_usuario_auth()
    kit_id_a_eliminar = 7  # Usando el ID proporcionado
    if token_auth:
        response = eliminar_kit(token_auth=token_auth)
        assert response.status_code == 204  # Asumiendo código 204 para éxito en la eliminación (No Content)