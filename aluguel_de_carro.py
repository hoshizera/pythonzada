km = float(input('Quantidade de kilometros percorrida: '))
dia = int(input('Quantos dias o carro ficou alugado: '))
valor = (dia * 60) + (km * 0.15)
print('Você gastou {:.2f}R$ alugando o carro.'.format(valor))
