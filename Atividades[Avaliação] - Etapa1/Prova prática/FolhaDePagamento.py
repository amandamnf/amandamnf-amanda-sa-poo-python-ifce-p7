from MovimentoFolha import MovimentoFolha
class FolhaPagamento:
    def __init__(self, mes, ano, totalDescontos, totalProventos):
        self._mes = mes
        self._ano = ano
        self._totalDescontos = totalDescontos
        self._totalProventos = totalProventos
        self._listaMovimentos = []
        self._listaColaboradores = []

    def addColaborador(self, colaborador):
        self._listaColaboradores.append(colaborador)

    def inserirmovimento1(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._listaMovimentos.append(movimento)

    def salarioSoma(self):
        total_salario = 0
        for colaborador in self._listaColaboradores:
            total_salario += colaborador.retornaSalarioAtual()
        return total_salario

    def calcularFolha(self):
        for movimento in self._listaMovimentos:
            if movimento.retornaTipMov().value == 1:
                self._totalProventos += movimento.getValor()
            else:
                self._totalDescontos += movimento.getValor()
        total_pagar = (self.salarioSoma() + self._totalProventos) - self._totalDescontos
        linhas = '=' * 111
        finalFollha = '{}' \
                      '\nTotal de Salários =  {:>50}\n' \
                      'Total de Proventos =   {:>50}\n' \
                      'Total de Descontos =   {:>50}\n' \
                      'Total a Pagar =        {:>50}\n' \
                      '{:>50}'.format(linhas, self.salarioSoma(), self._totalProventos, self._totalDescontos,
                                      total_pagar, linhas)
        return str(finalFollha)
