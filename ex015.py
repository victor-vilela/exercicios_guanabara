dias = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foi percorrido? '))

qtd_km = km * 0.15
qtd_dias = dias * 60
total = qtd_km + qtd_dias

print('O total a pagar é de R${:.2f}'.format(total))
