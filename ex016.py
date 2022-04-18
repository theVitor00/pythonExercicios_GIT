# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA.
# EX: 6.127 TEM A PARTE INTEIRA 6

from math import trunc

num = float(input('Digite um número Real: '))
print('{} tem como parte inteira o número {}.'.format(num, trunc(num)))

