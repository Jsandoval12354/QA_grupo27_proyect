
CREATE_USER_PAYLOAD = {
    "email": "test_user_unique@gmail.com",
    "password": "password123"
}

KIT_TEST_DATA = {
    "valid_name_kit": {"name": "Mi conjunto"},
    "long_valid_name_kit": {"name": "A" * 511 + "C"},
    "invalid_long_name_kit": {"name": "A" * 512 + "D"},
    "special_chars_kit": {"name": "~!@#$%^&*()_+=-`"},
    "spaces_kit_name": {"name": "Un nombre con espacios"},
    "numbers_kit_name": {"name": "Nombre123"},
    "empty_kit_name": {"name": ""},
    "missing_kit_name": {}
}

UPDATE_KIT_DATA = {
    "name": "Mi conjunto actualizado"
}