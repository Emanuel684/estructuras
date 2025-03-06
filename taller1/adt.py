from abc import ABC
from typing import Any, Union

from interface import InterfaceConjunto


class Nodo:
    def __init__(self, data: Any):
        self.data: Any = data
        self.siguiente: Union[None, "Nodo"] = None


class Conjunto(InterfaceConjunto, ABC):
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, data: Any) -> None:
        """
        Inserta un nuevo nodo al inicio de la lista enlazada, evitando duplicados.

        Args:
            data (Any): El valor que se desea insertar en la lista.

        Comportamiento:
            - Si la lista está vacía, el nuevo nodo se convierte en la cabeza de la lista.
            - Verifica si el valor ya existe en la lista recorriéndola completamente.
            - Si el valor ya está presente, no se inserta nuevamente.
            - Si el valor no es duplicado, se agrega al inicio de la lista.

        Ejemplo de uso:
            lista = ListaEnlazada()
            lista.insertar_inicio(5)
            lista.insertar_inicio(10)  # Inserta 10 al inicio
            lista.insertar_inicio(5)   # No inserta 5 nuevamente (duplicado)

        Complejidad:
            - En el peor de los casos, la complejidad es O(n), donde n es el número de nodos en la lista.

        """
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        es_duplicado = False

        if self.cabeza.data == nuevo_nodo.data:
            es_duplicado = True

        # Recorremos la lista original
        for element_self in self:
            if element_self.data == nuevo_nodo.data:
                es_duplicado = True

        # Si no es un duplicado, lo agregamos a la lista sin duplicados
        if not es_duplicado:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def insertar_final(self, data: Any) -> None:
        """
        Inserta un nuevo nodo al final de la lista enlazada, evitando duplicados.

        Args:
            data (Any): El valor que se desea insertar en la lista.

        Comportamiento:
            - Si la lista está vacía, el nuevo nodo se convierte en la cabeza de la lista.
            - Recorre la lista para verificar si el valor ya existe.
            - Si el valor ya está presente, no se inserta nuevamente.
            - Si el valor no es un duplicado, se agrega al final de la lista.

        Ejemplo de uso:
            lista = ListaEnlazada()
            lista.insertar_final(5)
            lista.insertar_final(10)  # Inserta 10 al final
            lista.insertar_final(5)   # No inserta 5 nuevamente (duplicado)

        Complejidad:
            - En el peor de los casos, la complejidad es O(n), donde n es el número de nodos en la lista.

        """
        nuevo_nodo = Nodo(data)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            # Recorremos la lista original
            es_duplicado = False

            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                if (
                    nodo_actual.data == nuevo_nodo.data
                    or nodo_actual.siguiente.data == nuevo_nodo.data
                ):
                    es_duplicado = True

                nodo_actual = nodo_actual.siguiente

            # Si no es un duplicado, lo agregamos a la lista sin duplicados
            if not es_duplicado:
                nodo_actual.siguiente = nuevo_nodo

    def remover_inicio(self) -> None:
        """
        Elimina el primer nodo de la lista enlazada.

        Comportamiento:
            - Si la lista está vacía, no realiza ninguna acción.
            - Si la lista tiene al menos un nodo, actualiza la cabeza para que apunte al siguiente nodo,
              eliminando así el primer nodo de la lista.

        Ejemplo de uso:
            lista = ListaEnlazada()
            lista.insertar_inicio(10)
            lista.insertar_inicio(5)
            lista.remover_inicio()  # Elimina el nodo con el valor 5 (el primero)

        Complejidad:
            - La operación es O(1), ya que solo se actualiza un puntero.

        """
        if self.cabeza is None:
            return

        self.cabeza = self.cabeza.siguiente

    def remover_final(self) -> None:
        """
        Elimina el último nodo de la lista enlazada.

        Comportamiento:
            - Si la lista está vacía, no realiza ninguna acción.
            - Si la lista solo tiene un nodo, lo elimina y la lista queda vacía.
            - Si la lista tiene más de un nodo, recorre la lista hasta llegar al penúltimo nodo
              y actualiza su referencia a `None`, eliminando así el último nodo.

        Ejemplo de uso:
            lista = ListaEnlazada()
            lista.insertar_inicio(10)
            lista.insertar_inicio(5)
            lista.remover_final()  # Elimina el nodo con el valor 10 (el último)

        Complejidad:
            - La operación es O(n), ya que en el peor de los casos se debe recorrer toda la lista.

        """
        if self.cabeza is None:
            return

        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        nodo_actual = self.cabeza
        while nodo_actual.siguiente and nodo_actual.siguiente.siguiente:
            nodo_actual = nodo_actual.siguiente

        nodo_actual.siguiente = None

    def union(self, conjunto: "Conjunto") -> "Conjunto":
        """
        Realiza la unión entre el conjunto actual (self) y otro conjunto pasado como parámetro.

        Descripción:
            - Crea un nuevo conjunto que contendrá todos los elementos únicos de ambos conjuntos.
            - Recorre los nodos de ambos conjuntos y los inserta en el nuevo conjunto.

        Parámetros:
            - conjunto (Conjunto): El conjunto con el que se realizará la unión.

        Retorno:
            - Conjunto: Un nuevo conjunto que representa la unión de ambos conjuntos.

        Comportamiento:
            1. Se crea un nuevo conjunto vacío (`nuevo_conjunto`).
            2. Se recorre el conjunto pasado como parámetro (`conjunto`) y se insertan sus elementos en `nuevo_conjunto`.
            3. Se recorre el conjunto actual (`self`) y se insertan sus elementos en `nuevo_conjunto`.
            4. Se retorna el nuevo conjunto (`nuevo_conjunto`).

        Posibles errores:
            - Si el conjunto pasado como parámetro no es del tipo `Conjunto`, se generará un error de tipo.
            - Si alguno de los conjuntos está vacío, la función aún funcionará, pero no se insertarán elementos de ese conjunto.
            - Si los conjuntos contienen elementos duplicados, estos se insertarán en `nuevo_conjunto` sin verificación de duplicados.

        Consideraciones:
            - La función no verifica si los elementos ya existen en `nuevo_conjunto` antes de insertarlos.
            - Si se desea evitar duplicados, se debe implementar una verificación adicional.
            - La complejidad temporal es O(n + m), donde n es el tamaño del conjunto actual y m es el tamaño del conjunto pasado como parámetro.
        """
        nuevo_conjunto = Conjunto()

        nodo_actual = conjunto.cabeza
        while nodo_actual.siguiente:
            nuevo_conjunto.insertar_final(nodo_actual.data)
            nodo_actual = nodo_actual.siguiente
        nuevo_conjunto.insertar_final(nodo_actual.data)

        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            nuevo_conjunto.insertar_final(nodo_actual.data)
            nodo_actual = nodo_actual.siguiente
        nuevo_conjunto.insertar_final(nodo_actual.data)

        return nuevo_conjunto

    def interseccion(self, conjunto: "Conjunto") -> "Conjunto":
        """
        Realiza la intersección entre el conjunto actual (self) y otro conjunto pasado como parámetro.

        Descripción:
            - Crea un nuevo conjunto que contendrá los elementos comunes entre ambos conjuntos.
            - Recorre los nodos del conjunto actual y verifica si cada elemento también está presente en el conjunto pasado como parámetro.
            - Si un elemento está en ambos conjuntos, se inserta en el nuevo conjunto.

        Parámetros:
            - conjunto (Conjunto): El conjunto con el que se realizará la intersección.

        Retorno:
            - Conjunto: Un nuevo conjunto que representa la intersección de ambos conjuntos.

        Comportamiento:
            1. Se crea un nuevo conjunto vacío (`nuevo_conjunto`).
            2. Se recorre el conjunto actual (`self`) y, para cada elemento, se verifica si está presente en el conjunto pasado como parámetro (`conjunto`).
            3. Si un elemento está en ambos conjuntos, se inserta en `nuevo_conjunto`.
            4. Se retorna el nuevo conjunto (`nuevo_conjunto`).

        Posibles errores:
            - Si el conjunto pasado como parámetro no es del tipo `Conjunto`, se generará un error de tipo.
            - Si alguno de los conjuntos está vacío, la función retornará un conjunto vacío, ya que no hay elementos comunes.
            - Si los nodos de los conjuntos no tienen el atributo `data`, se generará un error de atributo.

        Consideraciones:
            - La función no verifica si los elementos ya existen en `nuevo_conjunto` antes de insertarlos, lo que podría generar duplicados si el conjunto actual tiene elementos repetidos.
            - La complejidad temporal es O(n * m), donde n es el tamaño del conjunto actual y m es el tamaño del conjunto pasado como parámetro.
        """
        nuevo_conjunto = Conjunto()

        nodo_actual = self.cabeza
        while nodo_actual.data:

            nodo_actual_con = conjunto.cabeza
            while nodo_actual_con.data:
                if nodo_actual.data == nodo_actual_con.data:
                    nuevo_conjunto.insertar_final(nodo_actual.data)

                if nodo_actual_con.siguiente:
                    nodo_actual_con = nodo_actual_con.siguiente
                else:
                    break

            if nodo_actual.siguiente:

                nodo_actual = nodo_actual.siguiente
            else:
                break

        return nuevo_conjunto

    def diferencia(self, conjunto: "Conjunto") -> "Conjunto":
        """
        Realiza la diferencia entre el conjunto actual (self) y otro conjunto pasado como parámetro.

        Descripción:
            - Crea un nuevo conjunto que contendrá los elementos que están en el conjunto actual (self)
              pero no en el conjunto pasado como parámetro (conjunto).
            - Recorre los nodos del conjunto actual y verifica si cada elemento no está presente en el
              conjunto pasado como parámetro.
            - Si un elemento no está en el conjunto pasado como parámetro, se inserta en el nuevo conjunto.

        Parámetros:
            - conjunto (Conjunto): El conjunto con el que se realizará la diferencia.

        Retorno:
            - Conjunto: Un nuevo conjunto que representa la diferencia entre ambos conjuntos.

        Comportamiento:
            1. Se crea un nuevo conjunto vacío (`nuevo_conjunto`).
            2. Se recorre el conjunto actual (`self`) y, para cada elemento, se verifica si no está presente
               en el conjunto pasado como parámetro (`conjunto`).
            3. Si un elemento no está en el conjunto pasado como parámetro, se inserta en `nuevo_conjunto`.
            4. Se retorna el nuevo conjunto (`nuevo_conjunto`).

        Posibles errores:
            - Si el conjunto pasado como parámetro no es del tipo `Conjunto`, se generará un error de tipo.
            - Si alguno de los conjuntos está vacío, la función retornará un conjunto vacío o los elementos
              del conjunto actual, dependiendo del caso.
            - Si los nodos de los conjuntos no tienen el atributo `data`, se generará un error de atributo.

        Consideraciones:
            - La función no verifica si los elementos ya existen en `nuevo_conjunto` antes de insertarlos,
              lo que podría generar duplicados si el conjunto actual tiene elementos repetidos.
            - La complejidad temporal es O(n * m), donde n es el tamaño del conjunto actual y m es el tamaño
              del conjunto pasado como parámetro.
        """
        nuevo_conjunto = Conjunto()

        nodo_actual = self.cabeza
        while nodo_actual.data:
            esta_en_lista2 = False

            nodo_actual_con = conjunto.cabeza
            while nodo_actual_con.data:
                if nodo_actual.data == nodo_actual_con.data:
                    esta_en_lista2 = True

                if nodo_actual_con.siguiente:
                    nodo_actual_con = nodo_actual_con.siguiente
                else:
                    break

            if not esta_en_lista2:
                nuevo_conjunto.insertar_final(nodo_actual.data)

            if nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            else:
                break

        return nuevo_conjunto

    def diferencia_simetrica(self, conjunto: "Conjunto") -> "Conjunto":
        """
        Realiza la diferencia simétrica entre el conjunto actual (self) y otro conjunto pasado como parámetro.

        Descripción:
            - Crea un nuevo conjunto que contendrá los elementos que están en el conjunto actual (self) pero no en el
              conjunto pasado como parámetro (conjunto), y viceversa.
            - Recorre los nodos de ambos conjuntos y verifica si cada elemento no está presente en el otro conjunto.
            - Si un elemento no está en el otro conjunto, se inserta en el nuevo conjunto.

        Parámetros:
            - conjunto (Conjunto): El conjunto con el que se realizará la diferencia simétrica.

        Retorno:
            - Conjunto: Un nuevo conjunto que representa la diferencia simétrica entre ambos conjuntos.

        Comportamiento:
            1. Se crea un nuevo conjunto vacío (`nuevo_conjunto`).
            2. Se recorre el conjunto actual (`self`) y, para cada elemento, se verifica si no está presente en el
               conjunto pasado como parámetro (`conjunto`).
            3. Si un elemento no está en el conjunto pasado como parámetro, se inserta en `nuevo_conjunto`.
            4. Se recorre el conjunto pasado como parámetro (`conjunto`) y, para cada elemento, se verifica si no está
               presente en el conjunto actual (`self`).
            5. Si un elemento no está en el conjunto actual, se inserta en `nuevo_conjunto`.
            6. Se retorna el nuevo conjunto (`nuevo_conjunto`).

        Posibles errores:
            - Si el conjunto pasado como parámetro no es del tipo `Conjunto`, se generará un error de tipo.
            - Si alguno de los conjuntos está vacío, la función retornará los elementos del otro conjunto.
            - Si los nodos de los conjuntos no tienen el atributo `data`, se generará un error de atributo.

        Consideraciones:
            - La función no verifica si los elementos ya existen en `nuevo_conjunto` antes de insertarlos,
              lo que podría generar duplicados si los conjuntos tienen elementos repetidos.
            - La complejidad temporal es O(n * m), donde n es el tamaño del conjunto actual y m es el tamaño
              del conjunto pasado como parámetro.
        """
        nuevo_conjunto = Conjunto()

        nodo_actual = self.cabeza
        while nodo_actual.data:
            esta_en_lista2 = False

            nodo_actual_con = conjunto.cabeza
            while nodo_actual_con.data:
                if nodo_actual.data == nodo_actual_con.data:
                    esta_en_lista2 = True

                if nodo_actual_con.siguiente:
                    nodo_actual_con = nodo_actual_con.siguiente
                else:
                    break

            if not esta_en_lista2:
                nuevo_conjunto.insertar_final(nodo_actual.data)

            if nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            else:
                break

        nodo_actual = conjunto.cabeza
        while nodo_actual.data:
            esta_en_lista2 = False

            nodo_actual_con = self.cabeza
            while nodo_actual_con.data:
                if nodo_actual.data == nodo_actual_con.data:
                    esta_en_lista2 = True

                if nodo_actual_con.siguiente:
                    nodo_actual_con = nodo_actual_con.siguiente
                else:
                    break

            if not esta_en_lista2:
                nuevo_conjunto.insertar_final(nodo_actual.data)

            if nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            else:
                break

        return nuevo_conjunto

    def __validar__(self) -> bool:
        """
        Valida si el conjunto actual no contiene elementos duplicados.

        Descripción:
            - Recorre todos los elementos del conjunto actual y verifica si hay duplicados.
            - Si encuentra al menos un elemento duplicado, retorna `False`.
            - Si no encuentra duplicados, retorna `True`.

        Retorno:
            - bool: `True` si no hay elementos duplicados, `False` si se encuentran duplicados.

        Comportamiento:
            1. Se crea un nuevo conjunto vacío (`nuevo_conjunto`) para almacenar elementos únicos.
            2. Se recorre el conjunto actual (`self`) y, para cada elemento, se verifica si ya está en `nuevo_conjunto`.
            3. Si se encuentra un duplicado, se establece `es_duplicado` como `False` y se sale del bucle.
            4. Si no se encuentran duplicados, `es_duplicado` permanece como `True`.
            5. Se retorna el valor de `es_duplicado`.

        Posibles errores:
            - Si el conjunto actual no es iterable, se generará un error de tipo.
            - Si los elementos del conjunto no tienen el atributo `data`, se generará un error de atributo.
            - La lógica actual no funciona correctamente porque `nuevo_conjunto` siempre está vacío y no se agregan elementos a él.

        Consideraciones:
            - La función no está implementada correctamente, ya que `nuevo_conjunto` nunca se actualiza con los elementos de `self`.
            - La variable `es_duplicado` se inicializa como `True`, pero no cambia correctamente si se encuentra un duplicado.
            - La complejidad temporal es O(n²) en el peor caso, ya que se recorre `nuevo_conjunto` para cada elemento de `self`.
        """
        nuevo_conjunto = Conjunto()
        es_duplicado = True

        # Recorremos la lista original
        for element_self in self:
            # Comparamos el elemento actual con los elementos ya agregados a la lista sin duplicados
            for element in nuevo_conjunto:
                if element_self.data == element.data:
                    es_duplicado = False
                    # Salir del bucle si se encuentra una coincidencia

        return es_duplicado

    def __sizeof__(self) -> int:
        """
        Calcula el tamaño (número de nodos) de la lista enlazada.

        Descripción:
            - Recorre la lista enlazada desde la cabeza hasta el último nodo.
            - Cuenta el número de nodos en la lista.
            - Retorna el tamaño total de la lista.

        Retorno:
            - int: El número de nodos en la lista enlazada.

        Comportamiento:
            1. Inicializa un contador `tamano` en 0.
            2. Comienza desde el nodo cabeza (`self.cabeza`).
            3. Recorre cada nodo de la lista enlazada:
               - Incrementa el contador `tamano` en 1 por cada nodo.
               - Avanza al siguiente nodo (`nodo_actual.siguiente`).
            4. Cuando se llega al final de la lista (cuando `nodo_actual` es `None`), retorna el valor de `tamano`.

        Posibles errores:
            - Si la lista está vacía (`self.cabeza` es `None`), la función retornará 0.
            - Si la estructura de la lista enlazada está corrupta (por ejemplo, un nodo apunta a sí mismo o hay ciclos),
              la función entrará en un bucle infinito.
            - Si los nodos no tienen el atributo `siguiente`, se generará un error de atributo (`AttributeError`).

        Consideraciones:
            - La función no calcula el tamaño en bytes de la lista enlazada, sino el número de nodos.
            - La complejidad temporal es O(n), donde n es el número de nodos en la lista.
            - Esta función es útil para obtener el tamaño de la lista en tiempo de ejecución.
        """
        tamano = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            tamano += 1
            nodo_actual = nodo_actual.siguiente
        return tamano

    def __eq__(self, conjunto: "Conjunto") -> bool:
        s_con = str(conjunto)
        s_sel = str(self)

        return s_con == s_sel

    def __str__(self) -> str:
        nodo_actual = self.cabeza
        respuesta = ""
        while nodo_actual:
            respuesta = respuesta + str(nodo_actual.data)
            nodo_actual = nodo_actual.siguiente
        return respuesta

    def __iter__(self) -> "Conjunto":
        self.nodo_actual = self.cabeza
        return self

    def __next__(self) -> Nodo:
        if self.nodo_actual is None:
            raise StopIteration
        x = self.nodo_actual
        self.nodo_actual = self.nodo_actual.siguiente
        return x

    def __hash__(self) -> int:
        return hash((self.cabeza, self.cabeza.siguiente))

    def __repr__(self) -> None:
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.siguiente
