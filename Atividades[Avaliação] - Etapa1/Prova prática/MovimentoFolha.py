class MovimentoFolha:
    def __init__(self, colaborador, descricao, valor, tipoMovimento):
        self._colaborador = colaborador
        self._descricao = descricao
        self._valor = valor
        self._tipo_movimento = tipoMovimento

    def getValor(self):
        return self._valor

    def retornaTipMov(self):
        return self._tipo_movimento
