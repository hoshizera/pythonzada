from random import randint
from time import sleep
print('-'*36)
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('\033[36mVamos jogar JOKENPO!\033[m')
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada, Guerreiro do Leste? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
if jogador == comp:
    print('EMPATE, JOGUE DE NOVO =) !')
elif jogador == comp and comp == 2 or jogador == 1 and comp == 0 or jogador == 2 and comp == 1:
    print('-=' * 11)
    print('Você jogou {}'.format(itens[jogador]))
    print('Computador jogou {}'.format(itens[comp]))
    print('-='*11)
    print('VOCÊ GANHOU !!! =)')
elif jogador > 2:
    print('Selecione a opção correta =v')
else:
    print('-=' * 11)
    print('Você jogou {}'.format(itens[jogador]))
    print('Computador jogou {}'.format(itens[comp]))
    print('-=' * 11)
    print('VOCÊ PERDEU !!! =(')