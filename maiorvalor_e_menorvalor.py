n = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
menor = n
if n2<n and n2<n3:
    menor = n2
if n3<n and n3<n2:
    menor = n3
maior = n
if n2>n and n2>n3:
    maior = n2
if n3>n and n3>n2:
    maior = n3
print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))