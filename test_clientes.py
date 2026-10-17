from clientes import validar_cliente

def test_cliente_valido():
    assert validar_cliente(
        "Leandro Espinoza",
        "2212223333",
        "Calle 1 y 45"
    ) == True

def test_telefono_minimo():
    assert validar_cliente(
        "Leandro",
        "12345678",
        "Calle 1"
    ) == True

def test_telefono_maximo():
    assert validar_cliente(
        "Leandro",
        "123456789012345",
        "Calle 1"
    ) == True

def test_telefono_con_letras():
    assert validar_cliente(
        "Leandro",
        "1234ABCD",
        "Calle 1"
    ) == False

def test_nombre_vacio():
    assert validar_cliente(
        "",
        "2212223333",
        "Calle 1"
    ) == False

def test_direccion_vacia():
    assert validar_cliente(
        "Leandro",
        "2212223333",
        ""
    ) == False

def test_nombre_corto():
    assert validar_cliente(
        "Al",
        "2212223333",
        "Calle 1"
    ) == False

def test_telefono_9_digitos():
    assert validar_cliente(
        "María",
        "123456789",
        "Calle 21 y 525"
    ) == True

def test_telefono_14_digitos():
    assert validar_cliente(
        "Analía",
        "22111134567890",
        "Calle 333 y 53"
    ) == True

def test_nombre_3_letras():
    assert validar_cliente(
        "Ana",
        "2212223333",
        "Calle 1 y 45"
    ) == True