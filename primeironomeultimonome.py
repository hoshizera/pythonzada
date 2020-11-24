nome = str(input('Insira seu nome: ')).strip()
nome = nome.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Terceiro nome: {}'.format(nome[len(nome) - 1]))