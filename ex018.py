# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SEU SENO, COSSENO E TANGENTE

from math import sin, cos, tan

angulo = int(input('Digite o valor do ângulo a ser analisado: '))
print('-' * 41)
print('==== Analisando o ângulo de {} graus ===='.format(angulo))
print('SENO: {:.2f}'.format(sin(angulo)))
print('COSSENO: {:.2f}'.format(cos(angulo)))
print('TANGENTE: {:.2f}'.format(tan(angulo)))
print('-' * 41)
