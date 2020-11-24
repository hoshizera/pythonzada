casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
prest = casa / (anos*12)
min = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' A prestação será de R${:.2f}'.format(prest))
if prest <= min:
    print('Empréstimo pode ser REALIZADO!')
else:
    print('Empréstimo foi NEGADO!')
