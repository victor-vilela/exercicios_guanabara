salario = float(input('Digite o salário do funcionário: '))

if salario > 1250.00:
    aum_10 = salario + (salario * 0.1)
    print('O salário do funcionário teve um aumento de 10% que resultou em '
          'R${:.2f}'.format(aum_10))
else:
    aum_15 = salario + (salario * 0.15)
    print('O salário do funcionário teve um aumento de 15% que resultou em '
          'R${:.2f}'.format(aum_15))
