"""Moludo para criar uma fila prioritaria."""


from typing import List, Dict, Union
from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    """Classe que define uma fila prioritaria."""

    codigo: int = 0
    fila: List[str] = []
    cliente_atendidos: List[str] = []
    senha_atual = ""

    def gera_senha_atual(self) -> None:
        """Gera uma senha para um cliente."""
        self.senha_atual = f'PR{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        """Chama um cliente para um caixa especifico.

        Args:
            caixa (int): numero do caixa

        Returns:
            str: mensagem de qual cliente deve ir em qual caixa.
        """
        cliente_atual = self.fila.pop(0)
        self.cliente_atendidos.append(cliente_atual)

        return (f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}")
