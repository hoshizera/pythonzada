from random import randint
n = int(input('Digite um número de 1 a 5: '))
nr = randint(1, 5)
if n == nr:
    print('PARABÉNS, VOCÊ ACERTOU!)
else:
    print('Tente de novo, você ERROU! O número é: {}' .format(nr))