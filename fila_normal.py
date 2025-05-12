"""Cria uma fila normal."""


from typing import List
from fila_base import FilaBase
from constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):
    """Cria uma fila normal.

    Args:
        FilaBase (Class): classe de fila base.
    """

    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        """Gera a senha para a fila."""
        self.senha_atual = f'{CODIGO_NORMAL}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        """Chama o cliente para um caixa.

        Args:
            caixa (str): Nome do caixa

        Returns:
            str: Texto contendo o numero do cliente e qual o caixa.
        """
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}")