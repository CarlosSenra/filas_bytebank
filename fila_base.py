"""Modulo que implemneta a estrutura de uma fila base."""


import abc
from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    """Classe que define uma fila base."""

    codigo: int = 0
    fila = []
    cliente_atendidos = []
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

    @abc.abstractmethod
    def gera_senha_atual(self):
        """Define metodo abistrato de gerar senha."""
        ...

    @abc.abstractmethod
    def chama_cliente(self):
        """Define metodo abistrato de chamar cliente."""
        ...
