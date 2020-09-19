print('='*10,'LOJAS VILELA','='*10)

preco_compras = float(input('Preço das compras: R$'))
print('FORMA DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro/cheque\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    preco_final = preco_compras - (preco_compras * 0.1)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco_compras, preco_final))
elif opcao == 2:
    preco_final = preco_compras - (preco_compras * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco_compras, preco_final))
elif opcao == 3:
    print('Sua compra final é de R${:.2f}.'.format(preco_compras))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco_final = preco_compras + (preco_compras * 0.2)
    preco_parcelado = preco_final / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, preco_parcelado))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco_compras, preco_final))
else:
    print('Essa opção não existe.')
