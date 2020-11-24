d = float(input('Insira a distância em KM: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('E o preço de sua passagem sera: R${:.2f}'.format(preço))