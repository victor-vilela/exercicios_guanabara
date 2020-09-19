# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²

l = int(input('Digite a largura da parede: '))
h = int(input('Digite a altura da parede: '))

a = l * h
qtd_tinta = a / 2

print('A parede tem uma área de {}m² e a '
      'quantidade de tinta necessária será de {}L'.format(a, qtd_tinta))
