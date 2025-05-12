"""Modulo que implemneta a estrutura de uma fila base."""


class FilaBase:
    """Classe que define uma fila base."""

    codigo: int = 0
    fila = []
    cliente_atendidos = []
    senha_atual = ""

    def reseta_fila(self) -> None:
        """Metodo que reseta o codigo da fila quando ela chegar.
        
        Incrementa o codigo ate atingir 100, depois zera.
        """  # noqa: W293
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1