v = float(input('Digite a velocidade do carro: '))

if v > 80:
    print('Você foi multado!')
    multa = (v - 80) * 7
    print('Sua multa é no valor de R${:.2f}'.format(multa))
else:
    print('Velocidade abaixo do limite!')
