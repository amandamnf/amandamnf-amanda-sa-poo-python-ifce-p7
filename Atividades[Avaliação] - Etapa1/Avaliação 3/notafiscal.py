"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
# from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0

    def mostraData(self):
        listaDataHora = str(self._data).split()
        dataOnly = listaDataHora[0].split('-')
        dataMostrada = f'{dataOnly[2]}/{dataOnly[1]}/{dataOnly[0]}'
        return dataMostrada
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item.getValorItem()
        self._valorNota = valor

    def getValor(self):
        return self._valorNota
     
    def imprimirNotaFiscal(self):

        pontilhado = '-' * 111
        tracoFinal = '_' * 111

        finalNotaFormatada = ''

        if len(self._itens) > 0:
            for item in self._itens:
                finalNotaFormatada += '\n\n{}{:>3}{}'.format(item.getSequencial(), ' ', item.getDescricao())
                finalNotaFormatada += ' ' * (60 - len(item.getDescricao()))
                finalNotaFormatada += '{:.2f}             {:.2f}                  {:.2f}'.format(
                    item.getQuantidade(), item.getValorUnitario(),
                    item.getValorItem())

        finalNotaFormatada += '\n{}\nValor Total: {:.2f}'.format(tracoFinal, self._valorNota)

        print(pontilhado)
        print('NOTA FISCAL{:>100}'.format(self.mostraData()))
        print('Cliente:{:>6}{:>4}Nome: {}'.format(self._cliente.getCodigo(), ' ', self._cliente.getNome()))
        print('CPF/CNPJ: {}'.format(self._cliente.getCpfcpnj()))
        print(pontilhado)
        print('ITENS')
        print(pontilhado)
        print('Seq{:>3}Descrição{:>52}QTD{:>7}Valor Unit{:19}Preço'.format(' ', ' ', ' ', ' '))
        print('{}  {}    {}     {}     {}'.format('-' * 4, '-' * 56, '-' * 5, '-' * 12, '-' * 18))
        print(finalNotaFormatada)

    
    