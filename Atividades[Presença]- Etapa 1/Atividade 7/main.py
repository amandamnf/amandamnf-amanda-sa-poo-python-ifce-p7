from musica import Musica
from playlist import Playlist


musica1 = Musica('Tiago Carvalho', 'Deepest Cave', 'Wreck')
musica2 = Musica('Tiago Carvalho', 'Perfect Harmony', 'Wreck')
musica3 = Musica('Tiago Carvalho', 'Once', 'Wreck')
musica4 = Musica('Tiago Carvalho', 'Odd Phenomena', 'Wreck')

playlist1 = Playlist('Favoritas', 4)
playlist1.addmusica(musica1)
playlist1.addmusica(musica2)
playlist1.addmusica(musica3)
playlist1.addmusica(musica4)

mensagem, playlist1_ordenada = playlist1.ordenamusicas()
print(mensagem)
for musica in playlist1_ordenada:
    print(musica)

musica1.play()
musica1.pausar()
musica3.play()
musica3.pular()
musica4.play()
musica4.pausar()
musica4.sair()
musica2.play()
musica2.voltar()
