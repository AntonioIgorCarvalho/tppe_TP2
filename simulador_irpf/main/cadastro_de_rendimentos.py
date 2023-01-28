from .rendimento import Rendimento
from exceptions.exceptions import (DescricaoEmBrancoException,ValorRendimentoInvalidoException)
from .metodos_validacoes import *

class CadastroDeRendimentos:
    def __init__(self):
        self._rendimentos: list[Rendimento] = []
    
    def getTotalRendimentos(self) -> float:
        total: float = 0
        for rendimento in self._rendimentos:
            total = total + rendimento.getValor()

        return total

    def cadastrarRendimento(self, descricao, valor):
        if valorInvalido(valor):
            raise ValorRendimentoInvalidoException
        if descricaoInvalida(descricao):
            raise DescricaoEmBrancoException
        novoRendimento = Rendimento(descricao, valor)
        self._rendimentos.append(novoRendimento)