from matriz import Matriz

if __name__ == "__main__":
    # Caso 1: Sistema con solución única
    matriz = Matriz(3, 4)
    matriz.asignar(0, 0, 2)
    matriz.asignar(0, 1, 1)
    matriz.asignar(0, 2, -1)
    matriz.asignar(0, 3, 8)
    matriz.asignar(1, 0, -3)
    matriz.asignar(1, 1, -1)
    matriz.asignar(1, 2, 2)
    matriz.asignar(1, 3, -11)
    matriz.asignar(2, 0, -2)
    matriz.asignar(2, 1, 1)
    matriz.asignar(2, 2, 2)
    matriz.asignar(2, 3, -3)

    soluciones = matriz.eliminacion_gaussiana()
    print("soluciones: ", soluciones)
    assert round(soluciones[0]) == 2
    assert round(soluciones[1]) == 3
    assert round(soluciones[2]) == -1

    # Caso 2: Sistema sin solución (matriz singular)
    matriz_singular = Matriz(2, 3)
    matriz_singular.asignar(0, 0, 1)
    matriz_singular.asignar(0, 1, 2)
    matriz_singular.asignar(0, 2, 3)
    matriz_singular.asignar(1, 0, 2)
    matriz_singular.asignar(1, 1, 4)
    matriz_singular.asignar(1, 2, 6)

    try:
        matriz_singular.eliminacion_gaussiana()
    except ZeroDivisionError as e:
        print("Validacion correcta")
    else:
        # Solo se ejecuta esta parte del codigo si la validacion es correcta
        raise ZeroDivisionError("Fue permitida en la funcion eliminacion_gaussiana")
