# Faça um programa que leia um número inteiro e
# mostre na tela o seu sucessor e antecessor

n = int(input('Digite um número: '))
sucessor = n + 1
antecessor = n - 1

print('O número {} tem o sucessor {} e o antecessor {}'.format(n, sucessor, antecessor))