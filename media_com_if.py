n1 = float(input('Insira sua nota: '))
n2 = float(input('Insira sua nota: '))
print('Analisando...')
if (n1 + n2) / 2 <5.0:
    print('Você está REPROVADO!')
elif (n1 + n2) / 2 >= 5.0 and (n1 + n2) / 2 <= 6.9:
    print('Você está de RECUPERAÇÃO')
elif (n1 + n2) / 2 >= 7.0:
    print('Você está APROVADO! PARABÉNS')