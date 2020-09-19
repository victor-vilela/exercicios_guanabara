import math

cat_op = float(input('Digite o valor do cateto oposto: '))
cat_adj = float(input('Digite o valor do cateto adjacente: '))

hip = math.hypot(cat_op, cat_adj)

print('O comprimento da hipotenusa é {:.2f}'.format(hip))
