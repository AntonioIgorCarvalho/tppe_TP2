from .deducao import Deducoes

class TotalDeducoes:
    def __init__(self, deducoes: Deducoes) -> None:
        self.quantidadeDependentes: int = deducoes.getQtdeDependente()
        self.deducaoPorDependendte: float = 189.59
        self.totalValorDeducao: float = deducoes.totalValorDeducao

    def calculoValorTotalDeducoes(self)-> float:
        deducaoDependentes: float = self.deducaoPorDependendte * self.quantidadeDependentes
        totaldasDeducoes: float = deducaoDependentes + self.totalValorDeducao
        return round(totaldasDeducoes, 2)