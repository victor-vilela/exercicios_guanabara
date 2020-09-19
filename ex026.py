frase = input('Digite uma frase: ')

qtd_letra_a = frase.upper().count('A')
posicao_prm_a = frase.upper().find('A')
posicao_ult_a = frase.upper().rfind('A')

print("""
Na frase: "{}",
existem {} letras "a",
a primeira letra "a" está na posição {} e
a última letra "a" está na posição {}.
""".format(frase, qtd_letra_a, posicao_prm_a, posicao_ult_a))
