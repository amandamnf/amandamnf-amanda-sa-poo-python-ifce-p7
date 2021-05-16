dicionario = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
              'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
              'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
print('Escreva uma mensagem e esta será traduzida em código morse:\n')
frase = input('Mensagem: ')
caracteresmorse = []
for x in range(len(frase)):  # Percorre todos os caracteres da string em frase
    caractere = frase[x].lower()  # Deixa todos minúsculos primeiro para depois encontrá-los no dicionário
    if caractere in dicionario.keys():  # pois o dicionário possui apenas caracteres minúsculos
        caracteresmorse.append(caractere)  # Se esse caractere existir no dicionário, é adicionado também na lista
        # de caracteres a serem traduzidos

retornatraducaodoscaracteres = list(map(lambda c: dicionario[c], caracteresmorse))  # Traduz um por um os caracteres da lista caracteres[]
mensagememmorse = ' '.join(retornatraducaodoscaracteres)  # Transforma a lista anterior numa string normal, juntando os caracteres com espaços
print(f'A mensagem traduzida em código morse é: {mensagememmorse}')  # Mensagem traduzida
