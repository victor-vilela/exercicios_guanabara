from datetime import date

ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today()
faixa = ano_atual.year - ano

if faixa <= 9:
    print('MIRIM')
elif faixa > 9 and faixa <= 14:
    print('INFANTIL')
elif faixa > 14 and faixa <= 19:
    print('JUNIOR')
elif faixa == 20:
    print('SÊNIOR')
else:
    print('MASTER')
