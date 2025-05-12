"""Cria uma fila normal."""


from fila_base import FilaBase


class FilaNormal(FilaBase):
    """Cria uma fila normal.

    Args:
        FilaBase (Class): classe de fila base.
    """

    codigo: int = 0
    fila = []
    clientesatendidos = []
    senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        """Gera a senha para a fila."""
        self.senhaatual = f'NM{self.codigo}'

    def chama_cliente(self, caixa: str) -> str:
        """Chama o cliente para um caixa.

        Args:
            caixa (str): Nome do caixa

        Returns:
            str: Texto contendo o numero do cliente e qual o caixa.
        """
        cliente_atual: str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return (f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}")
