"""Modulo para por as filas para funcionar."""


from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila

fila_teste = FabricaFila.pega_fila('normal')

fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))

fila_teste2 = FabricaFila.pega_fila('prioritaria')

fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(5))
print(fila_teste2.chama_cliente(10))
print(fila_teste2.estatistica('10/05/2025', 215, 'detail'))
