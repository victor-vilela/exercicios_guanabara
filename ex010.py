# Crie um programa que leia quanto dinheiro umapessoa tem na carteira e
# mostre quantos dólares ela pode comprar. OBS: dolar = 3.27

real = float(input('Quantos reais tem na carteira: '))

dolar = real / 3.27

print('Na carteira tem R${:.2f} e pode comprar U${:.2f}'.format(real, dolar))
