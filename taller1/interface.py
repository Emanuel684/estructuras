from abc import ABC, abstractmethod
from typing import Any

from adt import Conjunto, Nodo


class InterfaceConjunto(ABC):

    @abstractmethod
    def insertar_inicio(self, data: Any) -> None:
        pass

    @abstractmethod
    def insertar_final(self, data: Any) -> None:
        pass

    @abstractmethod
    def remover_inicio(self) -> None:
        pass

    @abstractmethod
    def remover_final(self) -> None:
        pass

    @abstractmethod
    def union(self, conjunto: "Conjunto") -> "Conjunto":
        pass

    @abstractmethod
    def interseccion(self, conjunto: "Conjunto") -> "Conjunto":
        pass

    @abstractmethod
    def diferencia(self, conjunto: "Conjunto") -> "Conjunto":
        pass

    @abstractmethod
    def diferencia_simetrica(self, conjunto: "Conjunto") -> "Conjunto":
        pass

    @abstractmethod
    def __validar__(
        self,
    ) -> bool:
        pass

    @abstractmethod
    def __sizeof__(self) -> int:
        pass

    @abstractmethod
    def __eq__(self, conjunto: "Conjunto"):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __iter__(self) -> "Conjunto":
        pass

    @abstractmethod
    def __next__(self) -> "Nodo":
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> None:
        pass
