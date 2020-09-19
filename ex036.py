valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Qual é o seu salário? R$'))
qtd_anos = int(input('Quantos anos irá pagar? '))

valor_prestacao = valor_casa / (qtd_anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos, '
      'a pestação será de R${:.2f}'.format(valor_casa, qtd_anos, valor_prestacao))
if salario * 0.3 < valor_prestacao:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo APROVADO')
