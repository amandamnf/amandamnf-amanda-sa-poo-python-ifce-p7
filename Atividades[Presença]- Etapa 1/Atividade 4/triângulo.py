print('Insira abaixo o tamanho dos lados de um triângulo e diremos se ele é equilátero, isósceles ou escaleno.')


ladoA = int(input('Lado A: '))
ladoB = int(input('Lado B: '))
ladoC = int(input('Lado C: '))


if ladoA == ladoB and ladoB == ladoC:
    print('Equilátero')
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print('Isósceles')
else:
    print('Escaleno')