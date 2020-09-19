r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float (input('Terceira reta: '))

if r1 + r2 < r3 or r2 + r3 < r1 or r1 + r3 < r2:
    print('Não possível formar um triangulo')
elif r1 != r2 != r3 != r1:
    print('É possível formar um triângulo')
    print('É um triângulo escaleno')
elif r1 == r2 == r3:
    print('É possível formar um triângulo')
    print('É um triângulo equilátero')
else:
    print('É possível formar um triângulo')
    print('É um triângulo isósceles')
