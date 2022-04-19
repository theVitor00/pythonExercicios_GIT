# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE
# E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

from math import hypot
cateto_op = float(input('Digite o comprimento do cateto oposto: '))
cateto_adj = float(input('Digite o comprimeto do cateto adjacente: '))


print('O comprimento da hipotenusa é de {:.2f}'.format(hypot(cateto_op, cateto_adj)))


