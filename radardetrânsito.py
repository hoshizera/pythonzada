print('O limite de velocidade é de 80 KM/H')
carro = int(input('A velocidade do carro foi de:'))
if carro >80:
    print('Você foi multado por excesso de velocidade')
    multa = (carro - 80) * 7
    print("Você passou a {}KM/H e a sua multa foi de: R${:.2f}".format(carro, multa))
else:
    print('Obrigado por respeitar as leis de trânsito.')