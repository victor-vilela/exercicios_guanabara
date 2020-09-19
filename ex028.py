import random

num = random.randrange(6)

chute = int(input('Digite um número de 0 a 5: '))

if chute == num:
    print('Você acertou')
else:
    print('Você errou')
