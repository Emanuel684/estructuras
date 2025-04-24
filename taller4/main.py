from analisis_datos import AnalisisDatos

if __name__ == "__main__":
    # Cargar datos
    libros = AnalisisDatos.leerCSV("books.csv")

    # 1. Indexar por autor
    bst_autores = AnalisisDatos.indexarPorAutor(libros)

    # 2. Top M libros de un autor
    autor = "J.K. Rowling"
    m = 5
    top_libros = AnalisisDatos.topM(bst_autores, autor, m)

    print(f"Top {m} libros de {autor}:")
    for i, libro in enumerate(top_libros):
        print(f"{i + 1}. {libro}")

    # 3. Estadísticas por editorial
    stats_editorial = AnalisisDatos.estadisticasEditorial(libros)

    # 4. Top M editoriales
    AnalisisDatos.topMEditoriales(stats_editorial, 5)
