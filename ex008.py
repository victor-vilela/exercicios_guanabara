#Escreva um programa que leia um valor em metros e o exiba em
# centimetros e milimetros

m = int(input('Digite um valor em metros: '))

cm = m * 100
mm = m * 1000

print('{} metros convertendo para centimetros é {}cm e para milimetros é {}mm'.format(m, cm, mm))
