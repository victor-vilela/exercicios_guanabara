# Crie um algoritmo que leia um número e mostre o seu dobro, trilo e raiz quadrada

n = int(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raiz = n**(1/2)

print('O número {} tem o dobro como {}, o triplo como {} e sua raiz quadrada é {}'.format(n, dobro, triplo, raiz))
