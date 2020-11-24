print('As formas de pagamento disponíveis são: DINHEIRO/CHEQUE, CARTÃO, 2X E 3X (parcelas)')
p = float(input('Digite o preço: R$'))
cp = str(input('Digite a forma de pagamento: ')).lower()
cart = p / 100 * 5
cart = p - cart
din = p / 100 * 10
din = p - din
if cp =='dinheiro' or cp =='cheque':
    print('O preço ao pagar com a vista com dinheiro é R${}'.format(din))
elif cp =='cartão':
    print('O preço a vista com cartão é R${:.2f}'.format(cart))
elif cp =='2x':
    x = p / 2
    print('O valor da parcela em 2x é R${:.2f}'.format(x))
elif cp =='3x':
    x3 = p / 100 * 20
    x3 = p + x3
    print('O valor da parcela em 3x no total é de R${}'.format(x3))