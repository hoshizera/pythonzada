nome = str(input('Insira uma palavra: ')).upper().strip()
print('A letra A aparece {} vezes'.format(nome.count('A')))
print('Em que posição ela aparece pela primeira vez: {}'.format(nome.find('A')+ 1)) # + 1 PARA ELE NAO "COMEÇAR" DO ZERO E FICAR ESQUISITO PARA GENTE #
print(' A última letra A apareceu na posição: {}'.format(nome.rfind('A')+ 1))