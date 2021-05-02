from random import randint

numerosDaAposta = []

while len(numerosDaAposta) < 6:
    numero_aleatorio = randint(1, 60)

    if numero_aleatorio not in numerosDaAposta:
        numerosDaAposta.append(numero_aleatorio)


numerosDaAposta.sort()

print('Os números que você deve jogar são: {}'.format(numerosDaAposta))
