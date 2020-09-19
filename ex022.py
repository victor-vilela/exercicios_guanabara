nome = input('Digite o seu nome completo: ')

maiusculo = nome.upper()
minusculo = nome.lower()
qtd_letra_sem_espaco = len(nome.replace(' ', ''))
qtd_letra_primeiro_nome = nome.split()
qtd_letra_primeiro_nome = len(qtd_letra_primeiro_nome[0])

print("""
O nome {} 
em maiúsculo fica {},
em minúsculo fica {},
tem {} letras e
o primeiro nome tem {} letras.
""".format(nome, maiusculo, minusculo, qtd_letra_sem_espaco, qtd_letra_primeiro_nome))
