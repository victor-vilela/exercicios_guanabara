# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o valor do preço: R$'))

desc = preco * 0.05
novo_preco = preco - desc

print('O preço de R${:.2f} com 5% de desconto '
      'fica no valor de R${:.2f}'.format(preco, novo_preco))