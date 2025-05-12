"""Modulo que implemneta a estrutura de uma fila base."""


import abc
from typing import List, Union, Dict
from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    """Classe que define uma fila base."""

    codigo: int = 0
    fila: List[str] = []
    cliente_atendidos: List[str] = []
    senha_atual = ""

    def reseta_fila(self) -> None:
        """Metodo que reseta o codigo da fila quando ela chegar.
        
        Incrementa o codigo ate atingir 100, depois zera.
        """  # noqa: W293
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def insere_cliente(self):
        """Insere um cliente na fila."""
        self.fila.append(self.senha_atual)

    def atualiza_fila(self):
        """Atualiza a fila prioritaria."""
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    def estatistica(self, dia: str, agencia: int, flag: str) -> Dict:
        """Calcula estatisticas em relacao a fila prioritaria.

        Args:
            dia (str): Data que deseja a estatistisca. "01/01/1970".
            agencia (int): numero da agencia.
            flag (str): 'detail' ou qualquer outra coisa.

        Returns:
            dict: _description_
        """
        estatistica: Dict[str, Union[List[str], str, int]] = {}
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

    @abc.abstractmethod
    def gera_senha_atual(self):
        """Define metodo abistrato de gerar senha."""
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        """Define metodo abistrato de chamar cliente."""
        ...
