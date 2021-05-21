from FolhaDePagamento import FolhaPagamento
from Colaborador import Colaborador
from MovimentoFolha import MovimentoFolha
from TipoMovimento import TipoMovimento

Fp = FolhaPagamento(9, 2019, 0, 0)

Cl01 = Colaborador("100", "Manoel Claudino", "Av 13 de Maio 2081", "88671020", "Benfica", "60020-060", "124543556-89", 4500.00)
Cl02 = Colaborador("200", "Carmelina da Silva", "Avenida dos Expedicionários 1200", "3035-1280", "Aeroporto", "60530-020", "301789435-54", 2500.00)
Cl03 = Colaborador("300", "Gurmelina Castro Saraiva", "Av João Pessoa 1020", "3235-1089", "Damas", "60330-090", "350245632-76", 3000.00)

Mf01 = MovimentoFolha(Cl01, "Salario", 4500.00, TipoMovimento.P)
Mf02 = MovimentoFolha(Cl01, "Plano Saúde", 1000.00, TipoMovimento.P)
Mf03 = MovimentoFolha(Cl01, "Pensão", 600.00, TipoMovimento.D)
Mf04 = MovimentoFolha(Cl02, "Salario", 2500.00, TipoMovimento.P)
Mf05 = MovimentoFolha(Cl02, "Gratificação", 1000.00, TipoMovimento.P)
Mf06 = MovimentoFolha(Cl02, "Faltas", 600.00, TipoMovimento.D)
Mf07 = MovimentoFolha(Cl03, "Salario", 4500.00, TipoMovimento.P)
Mf08 = MovimentoFolha(Cl03, "Plano Saúde", 1000.00, TipoMovimento.P)
Mf09 = MovimentoFolha(Cl03, "Pensão", 600.00, TipoMovimento.D)

Fp.addColaborador(Cl01)
Fp.addColaborador(Cl02)
Fp.addColaborador(Cl03)

Fp.inserirmovimento1(Mf01)
Fp.inserirmovimento1(Mf02)
Fp.inserirmovimento1(Mf03)
Fp.inserirmovimento1(Mf04)
Fp.inserirmovimento1(Mf05)
Fp.inserirmovimento1(Mf06)
Fp.inserirmovimento1(Mf07)
Fp.inserirmovimento1(Mf08)
Fp.inserirmovimento1(Mf09)

Cl01.inserirmovimentos2(Mf01)
Cl01.inserirmovimentos2(Mf02)
Cl01.inserirmovimentos2(Mf03)
Cl02.inserirmovimentos2(Mf04)
Cl02.inserirmovimentos2(Mf05)
Cl02.inserirmovimentos2(Mf06)
Cl03.inserirmovimentos2(Mf07)
Cl03.inserirmovimentos2(Mf08)
Cl03.inserirmovimentos2(Mf09)

print(Cl01.calcularSalario())
print(Cl02.calcularSalario())
print(Cl03.calcularSalario())
print(Fp.calcularFolha())
