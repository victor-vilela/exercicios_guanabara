distancia = float(input('Digite a distância da viagem em Km: '))

if distancia < 200:
    passagem = distancia * 0.5
    print('Sua passagem é no valor de R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Sua passagem é no valor de R${:.2f}'.format(passagem))