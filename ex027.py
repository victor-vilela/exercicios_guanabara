nome = input('Digite seu nome completo: ')

nome_separado = nome.split()

print("""
Primeiro nome: {}
Último nome: {}
""".format(nome_separado[0], nome_separado[len(nome_separado) - 1]))
