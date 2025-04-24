class Valoracion:
    """
    Clase que representa un sistema de valoración de libros.

    Atributos:
        cantidad_libros (int): Número total de libros valorados.
        suma_ratings (float): Suma de todas las valoraciones realizadas.

    Métodos:
        promedio: Calcula el promedio de las valoraciones de los libros.
        agregar_libro(rating): Agrega una nueva valoración al sistema.
        __str__(): Devuelve una representación en cadena del sistema de valoración.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Valoracion con cero libros
        y una suma de valoraciones igual a 0.0.
        """
        self.cantidad_libros = 0
        self.suma_ratings = 0.0

    @property
    def promedio(self):
        """
        float: Calcula y devuelve el promedio de las valoraciones de los libros.
        Si no hay libros valorados, devuelve 0.0.
        """
        return (
            self.suma_ratings / self.cantidad_libros
            if self.cantidad_libros > 0
            else 0.0
        )

    def agregar_libro(self, rating):
        """
        Agrega una nueva valoración de libro al sistema.

        Args:
            rating (float): La valoración del libro que se va a agregar.
        """
        self.cantidad_libros += 1
        self.suma_ratings += rating

    def __str__(self):
        """
        Devuelve una representación en cadena del sistema de valoración.

        Returns:
            str: Una cadena en el formato "Libros: <cantidad_libros>, Rating promedio: <promedio>".
        """
        return f"Libros: {self.cantidad_libros}, Rating promedio: {self.promedio:.2f}"
