from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
play = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-='*11)
print('Você jogou {}.'.format(itens[play]))
print('O computador jogou {}'.format(itens[computador]))
print('-='*11)
if computador == 0: # Computador joga PEDRA
    if play == 0:
        print('EMPATE, JOGUE DE NOVO! :)')
    elif play == 1:
        print('VOCÊ GANHOU!! :)')
    elif play == 2:
        print('VOCÊ PERDEU!!! :(')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # Computador jogou PAPEL
    if play == 0:
        print('VOCÊ PERDEU !!! :(')
    elif play == 1:
        print('EMPATE, JOGUE DE NOVO! :)')
    elif play == 2:
        print('VOCÊ GANHOU!!! :)')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # Computador jogou TESOURA
    if play == 0:
        print('VOCÊ GANHOU!!! :)')
    elif play == 1:
        print('VOCÊ PERDEU!!! :(')
    elif play == 2:
        print('EMPATE, JOGUE DE NOVO!!! :)')
    else:
        print('JOGADA INVÁLIDA!')