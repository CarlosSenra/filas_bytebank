"""Moludo para criar uma fila prioritaria."""


from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    """Classe que define uma fila prioritaria."""

    codigo: int = 0
    fila = []
    cliente_atendidos = []
    senha_atual = ""

    def gera_senha_atual(self) -> None:
        """Gera uma senha para um cliente."""
        self.senha_atual = f'PR{self.codigo}'

    def atualiza_fila(self) -> None:
        """Atualiza a fila prioritaria."""
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

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

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        """Calcula estatisticas em relacao a fila prioritaria.

        Args:
            dia (str): Data que deseja a estatistisca. "01/01/1970".
            agencia (int): numero da agencia.
            flag (str): 'detail' ou qualquer outra coisa.

        Returns:
            dict: _description_
        """
        if flag != 'detail':
            estatistica = {f'{agencia}-{dia}': len(self.cliente_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.cliente_atendidos
            estatistica['quantidade_clientes_atendidos'] = (
                len(self.cliente_atendidos)
            )

        return estatistica