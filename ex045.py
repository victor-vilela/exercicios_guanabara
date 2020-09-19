import random

comp = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print(comp)

print('='*10, 'JOKENPÔ', '='*10)
print('[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA')
opcao = int(input('Sua opção: '))

if opcao == 1:
    if comp == 'PEDRA':
        print('EMPATE')
    elif comp == 'PAPEL':
        print('VOCÊ PERDEU')
    else:
        print('VOCÊ GANHOU')
elif opcao == 2:
    if comp == 'PEDRA':
        print('VOCÊ GANHOU')
    elif comp == 'PAPEL':
        print('EMPATE')
    else:
        print('VOCÊ PERDEU')
elif opcao == 3:
    if comp == 'PEDRA':
        print('VOCÊ PERDEU')
    elif comp == 'PAPEL':
        print('VOCÊ GANHOU')
    else:
        print('EMPATE')
else:
    print('Esta opção não existe')
