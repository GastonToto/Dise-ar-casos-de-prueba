def validar_cliente(nombre, telefono, direccion):
    if not nombre or len(nombre.strip()) < 3:
        return False

    if not telefono.isdigit():
        return False

    if len(telefono) < 8 or len(telefono) > 15:
        return False

    if not direccion.strip():
        return False

    return True