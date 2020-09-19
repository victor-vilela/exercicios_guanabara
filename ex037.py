num =int(input('Digite um número inteiro: '))
base = int(input('Qual base de conversão deseja:\n'
                 '1 para binário\n'
                 '2 para octal\n'
                 '3 para hexadecimal\n'
                 'Sua opção: '))

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Essa opção é inválida!')
