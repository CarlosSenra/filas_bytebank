"""Modulo que cria uma fabirca de filas."""


from typing import Union
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:
    """Classe que definem filas diferentes."""

    @staticmethod
    def pega_fila(tipo_fila: str) -> Union[FilaNormal, FilaPrioritaria]:
        """Metodo que pega uma fila de acordo com o tipo."""
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError("Tipo de fila nao existe")