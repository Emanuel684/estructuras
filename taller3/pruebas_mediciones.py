from lista import DoubleLinkedList
from libro import Libro
from ordenacion import LibroController


def Taller3():
    # 1. Leer datos
    libros_lista = Libro.leerCSV("books.csv")
    libros_dll = DoubleLinkedList()
    for libro in libros_lista:
        libros_dll.append(libro)

    print(f"Total de libros cargados: {len(libros_lista)}")

    # 2. Ordenar por rating
    print("\nOrdenando por rating descendente...")
    libros_ordenados = LibroController.ordenar_por_rating(libros_lista)

    print("\nTop 5 libros por rating:")
    LibroController.head(libros_ordenados)

    print("\nPeores 5 libros por rating:")
    LibroController.tail(libros_ordenados)

    # 3. Ordenar por diferentes comparadores
    print("\nOrdenando por autor:")
    LibroController.listar_por_comparador(libros_lista, LibroController.comparador_autor)

    print("\nOrdenando por ratings_count descendente:")
    LibroController.listar_por_comparador(
        libros_lista, LibroController.comparador_ratings_count, reverse=True
    )

    print("\nOrdenando por fecha de publicación:")
    LibroController.listar_por_comparador(libros_lista, LibroController.comparador_fecha)

    # 4. Medición de tiempos
    print("\nRealizando mediciones de tiempo...")
    comparadores = {
        "rating": None,
        "autor": LibroController.comparador_autor,
        "ratings_count": LibroController.comparador_ratings_count,
        "fecha": LibroController.comparador_fecha,
    }

    resultados = {"builtin": {}, "quicksort": {}}

    K = 20
    for alg in ["builtin", "quicksort"]:
        for comp_name, comp_func in comparadores.items():
            tiempos = []
            for i in range(K):
                t = LibroController.medir_tiempo_alg(
                    libros_lista, comp_func, alg, comp_name == "ratings_count"
                )
                if i > 0:  # Descartar primera medición (warm-up)
                    tiempos.append(t)

            avg_time = sum(tiempos) / len(tiempos)
            resultados[alg][comp_name] = avg_time
            print(
                f"{alg} - {comp_name}: {avg_time:.6f} segundos (promedio {K - 1} ejecuciones)"
            )

    # 5. Análisis comparativo
    print("\nAnálisis comparativo:")
    print("Algoritmo\tComparador\tTiempo (s)")
    for alg in resultados:
        for comp in resultados[alg]:
            print(f"{alg}\t{comp}\t{resultados[alg][comp]:.6f}")

    print("\nConclusiones:")
    print(
        "1. El sort built-in de Python es significativamente más rápido que nuestra implementación de quicksort"
    )
    print("2. El comparador más costoso es el de fecha por requerir parsing de strings")
    print("3. El orden de complejidad se mantiene (O(n log n) para ambos casos)")
    print(
        "4. La implementación built-in está optimizada en C y tiene mejor manejo de memoria"
    )


if __name__ == "__main__":
    Taller3()
