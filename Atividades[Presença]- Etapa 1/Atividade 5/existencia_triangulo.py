from funcao import func_verificacao

print('Insira 3 lados e verificaremos se é possível formar um triângulo com eles.')

x = int(input('Lado a do triângulo: '))
y = int(input('Lado b do triângulo: '))
z = int(input('Lado c do triângulo: '))

if func_verificacao(x, y, z):
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
