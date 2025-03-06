# ID = 000478429
import hashlib


def hash_equipo(ids):
    """
    Calcula el hash SHA-256 de la concatenación de los IDs y devuelve el módulo 5 del resultado.
    :param ids: Lista de IDs de los miembros del equipo.
    :return: Número de ejercicio (módulo 5 del hash).
    """
    # Concatenar los IDs
    concatenado = "".join(ids)

    # Calcular el hash SHA-256
    hash_sha256 = hashlib.sha256(concatenado.encode()).hexdigest()

    # Convertir el hash a un número entero
    hash_int = int(hash_sha256, 16)

    # Calcular el módulo 5
    return hash_int % 5


# Ejemplo de uso
ids = ["000478429"]  # Solo tu ID
numero_ejercicio = hash_equipo(ids)
print("Número de ejercicio:", numero_ejercicio)

# Otra forma de hacerlo

hash_hex = "e2401414757d4a0f6bafc633a2d1a212b2eea4dba427fd8b5c843f32269896d3"
hash_int = int(hash_hex, 16)  # Convertir de hexadecimal a entero
modulo = hash_int % 5  # Calcular el módulo 5
print("modulo: ", modulo)
