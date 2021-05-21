from MovimentoFolha import MovimentoFolha

class Colaborador:
    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salarioAtual):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._bairro = bairro
        self._cep = cep
        self._cpf = cpf
        self._salarioAtual = salarioAtual
        self._movimentos = []

    def inserirmovimentos2(self, movimento):
        if type(movimento) is MovimentoFolha:
            self._movimentos.append(movimento)

    def retornaSalarioAtual(self):
        return self._salarioAtual

    def calcularSalario(self):
        total_proventos = 0
        total_descontos = 0
        for movimento in self._movimentos:
            if movimento.retornaTipMov().value == 1:
                total_proventos += movimento.getValor()
            else:
                total_descontos += movimento.getValor()
        salario_liquido = self._salarioAtual + total_proventos - total_descontos
        linhas = '=' * 111
        dadosFinais = '{}\nCódigo:                {:>50}' \
                      '\nNome:                    {:>50}' \
                      '\nSalário:                 {:>50}' \
                      '\nTotal proventos:         {:>50}' \
                      '\nTotal descontos:         {:>50}' \
                      '\nValor líquido a receber: {:>50}' \
                      '\n' \
                      '{}'.format(linhas, self._codigo, self._nome,
                                  self._salarioAtual, total_proventos,
                                  total_descontos,
                                  salario_liquido, linhas)
        return str(dadosFinais)
