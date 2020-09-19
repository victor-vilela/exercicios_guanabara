from datetime import date

ano = int(input('Informe o ano de nascimento: '))
ano_atual = date.today()

if ano_atual.year - ano < 18:
    print('Você ainda irá se alistar ao serviço militar!')
elif ano_atual.year - ano == 18:
    print('É hora de alistar ao serviço militar!')
else:
    print('Já passou do tempo do alistamento militar!')
