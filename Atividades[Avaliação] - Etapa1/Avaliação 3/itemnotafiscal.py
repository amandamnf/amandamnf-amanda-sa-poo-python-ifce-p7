"""
    Módulo itemnotafiscal 
    Classe ItemNotaFiscal 
    Atributos :
        id         - informado
        sequencial - informado
        quantidade - informado
        produto    - informado
        valor      - calculado.            
"""
from produto import Produto

class ItemNotaFiscal():
    
  
    def __init__(self, id, sequencial, quantidade, produto):
        self._id=id
        self._sequencial=sequencial
        self._quantidade=quantidade
        self._produto=produto
        self._descricao=self._produto.getDescricao()
        self._valorUnitario=self._produto.getValorUnitario()
        self._valorItem=float(self._quantidade * self._valorUnitario)
      
    def str(self):
        string="\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(self._valorItem,
                                                                                                             self._valorUnitario,
                                                                                                             self._descricao, 
                                                                                                             self._quantidade, 
                                                                                                             self._sequencial, 
                                                                                                             self._id)
        return string

    def getSequencial(self):
        sequ=str(self._sequencial)
        if len(sequ) > 2:
            return sequ
        elif len(sequ) > 1:
            return f'0{sequ}'
        return f'00{sequ}'

    def getQuantidade(self):
        return self._quantidade

    def getDescricao(self):
        return self._descricao

    def getValorUnitario(self):
        return self._valorUnitario

    def getValorItem(self):
        return self._valorItem
    
        
if __name__ == '__main__':
    produto = Produto(1,100,'Arroz', 5.5) 
    item=ItemNotaFiscal(1, 1, 12, produto)
    print(item.str())
        
    

