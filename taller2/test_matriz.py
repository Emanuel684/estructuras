from matriz import Matriz

if __name__ == "__main__":
    # Igualdad
    matriz1 = Matriz(2, 2)
    matriz1.asignar(0, 0, 1)
    matriz1.asignar(0, 1, 2)
    matriz1.asignar(1, 0, 3)
    matriz1.asignar(1, 1, 4)
    print("matriz1:\n", matriz1)

    matriz2 = Matriz(2, 2)
    matriz2.asignar(0, 0, 1)
    matriz2.asignar(0, 1, 2)
    matriz2.asignar(1, 0, 3)
    matriz2.asignar(1, 1, 4)
    print("matriz2:\n", matriz2)

    matriz3 = Matriz(2, 2)
    matriz3.asignar(0, 0, 1)
    matriz3.asignar(0, 1, 2)
    matriz3.asignar(1, 0, 3)
    matriz3.asignar(1, 1, 5)
    print("matriz3:\n", matriz3)

    assert matriz1 == matriz2
    assert matriz1 != matriz3

    # Suma
    matriz1 = Matriz(2, 2)
    matriz1.asignar(0, 0, 1)
    matriz1.asignar(0, 1, 2)
    matriz1.asignar(1, 0, 3)
    matriz1.asignar(1, 1, 4)

    matriz2 = Matriz(2, 2)
    matriz2.asignar(0, 0, 5)
    matriz2.asignar(0, 1, 6)
    matriz2.asignar(1, 0, 7)
    matriz2.asignar(1, 1, 8)

    resultado = matriz1.suma(matriz2)
    esperado = Matriz(2, 2)
    esperado.asignar(0, 0, 6)
    esperado.asignar(0, 1, 8)
    esperado.asignar(1, 0, 10)
    esperado.asignar(1, 1, 12)
    print("Resultado Suma:\n", esperado)

    assert resultado == esperado

    # Producto
    matriz1 = Matriz(2, 3)
    matriz1.asignar(0, 0, 1)
    matriz1.asignar(0, 1, 2)
    matriz1.asignar(0, 2, 3)
    matriz1.asignar(1, 0, 4)
    matriz1.asignar(1, 1, 5)
    matriz1.asignar(1, 2, 6)

    matriz2 = Matriz(3, 2)
    matriz2.asignar(0, 0, 7)
    matriz2.asignar(0, 1, 8)
    matriz2.asignar(1, 0, 9)
    matriz2.asignar(1, 1, 10)
    matriz2.asignar(2, 0, 11)
    matriz2.asignar(2, 1, 12)

    resultado = matriz1.producto(matriz2)
    esperado = Matriz(2, 2)
    esperado.asignar(0, 0, 58)
    esperado.asignar(0, 1, 64)
    esperado.asignar(1, 0, 139)
    esperado.asignar(1, 1, 154)
    print("Resultado producto:\n", esperado)

    assert resultado == esperado
