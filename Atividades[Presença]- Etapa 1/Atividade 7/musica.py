class Musica:
    def __init__(self, cantor, nome, album):
        self._cantor = cantor
        self._nome = nome
        self._album = album

    def play(self):
        print(f"Você está escutando \"{self._nome}\" de \"{self._cantor}\"...")

    @staticmethod
    def pausar():
        print("Pausado.")

    @staticmethod
    def avancar():
        print("Você avançou 10s...")

    @staticmethod
    def retroceder():
        print("Você retrocedeu 10s...")

    @staticmethod
    def pular():
        print("Você pulou.")

    @staticmethod
    def voltar():
        print("Você voltou uma música...")

    @staticmethod
    def sair():
        print("Você saiu do player.")

    def getnome(self):
        return self._nome
