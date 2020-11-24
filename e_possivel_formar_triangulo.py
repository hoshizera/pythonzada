print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Digite um valor de reta: '))
r2 = float(input('Digite um valor de reta: '))
r3 = float(input('Digite um valor de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triângulo')
else:
    print('Não foi possível formar um triângulo')