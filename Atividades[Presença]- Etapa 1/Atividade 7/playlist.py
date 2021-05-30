class Playlist:
    def __init__(self, nome, quantidade):
        self._nome = nome
        self._quantidade = int(quantidade)
        self._lista = []

    def addmusica(self, musica):
        self._lista.append(musica)

    def ordenamusicas(self):
        listaordenada = []
        for musica in self._lista:
            listaordenada.append(musica.getnome())
        listaordenada.sort()
        _str = f'Playlist "{self._nome}" ordenada:'
        return _str, listaordenada

    def getlista(self):
        return self._lista
