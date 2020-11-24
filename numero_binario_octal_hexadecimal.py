n = int(input('Insira um número: '))
op = str(input('Escolha a operação desejada: ')).lower()
if op == 'binário':
    print('O resultado é {:b}'.format(n))
elif op =='octal':
    print('O número em numero octal é: {:o}'.format(n))
elif op == 'hexadecimal':
    print('O número em hexadecimal é: {:x}'.format(n))
